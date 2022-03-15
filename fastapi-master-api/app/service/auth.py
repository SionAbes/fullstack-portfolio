from datetime import datetime, timedelta
from typing import List, MutableMapping, Union

import jwt
from app.api.models.login_response import LoginResponse
from app.api.models.token import Token
from app.api.models.user import User
from app.domain.user import User as DomainUser
from app.repository.database.users import users_repo
from app.security import verify_string_hash
from app.service.exceptions import BadPasswordError, EntityNotFoundError
from app.settings import Settings
from sqlalchemy.orm.session import Session

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]


def authenticate(
    *, email: str, password: str, db: Session, settings: Settings
) -> LoginResponse:

    user: DomainUser = users_repo.get_by_email(db=db, email=email)

    if not user:
        raise EntityNotFoundError("user does not exist")
    if not verify_string_hash(password, user.password):
        raise BadPasswordError("users password is not correct")

    roles = ["USER"]
    if user.is_superuser:
        roles.append("ADMIN")

    token = create_access_and_refresh_token(
        user_id=user.id, roles=roles, settings=settings
    )

    return LoginResponse(
        user=User(
            id=user.id,
            last_login=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        ),
        refresh_token=token.refresh_token,
        access_token=token.access_token,
    )


def create_access_and_refresh_token(
    user_id: int, roles: List[str], settings: Settings
) -> Token:

    access_token = create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=user_id,
        roles=roles,
        settings=settings,
    )

    refresh_token = create_token(
        token_type="refresh_token",
        lifetime=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
        sub=user_id,
        roles=roles,
        settings=settings,
    )

    return Token(access_token=access_token, refresh_token=refresh_token)


def create_token(
    token_type: str, lifetime: timedelta, sub: int, roles: List[str], settings: Settings
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)
    payload["roles"] = roles

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
