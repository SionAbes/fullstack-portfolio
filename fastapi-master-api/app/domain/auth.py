from datetime import datetime, timedelta
from typing import List, MutableMapping, Union

import jwt
from app.api.models.login_response import LoginResponse
from app.api.models.token import Token
from app.api.models.user import User
from app.domain.exceptions import BadPasswordError, EntityNotFoundError
from app.domain.models.user import User as DomainUser
from app.repository.database.users import users_repo
from app.security import verify_password
from app.settings import get_settings
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session

settings = get_settings()

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_URL}/auth/login")


def authenticate(
    *,
    email: str,
    password: str,
    db: Session,
) -> LoginResponse:

    user: DomainUser = users_repo.get_by_email(db=db, email=email)

    if not user:
        raise EntityNotFoundError("user does not exist")
    if not verify_password(password, user.password):
        raise BadPasswordError("users password is not correct")

    roles = ["USER"]
    if user.is_superuser:
        roles.append("ADMIN")

    token = create_access_and_refresh_token(user_id=user.id, roles=roles)

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


def create_access_and_refresh_token(user_id: int, roles: List[str]) -> Token:

    access_token = create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=user_id,
        roles=roles,
    )

    refresh_token = create_token(
        token_type="refresh_token",
        lifetime=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
        sub=user_id,
        roles=roles,
    )

    return Token(access_token=access_token, refresh_token=refresh_token)


def create_token(
    token_type: str, lifetime: timedelta, sub: int, roles: List[str]
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)
    payload["roles"] = roles

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
