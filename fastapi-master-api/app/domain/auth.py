from typing import MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
import jwt
from app.repository.database.users import users_repo
from app.api.models.login_response import LoginResponse
from app.settings import get_settings
from app.domain.exceptions import EntityNotFoundError, BadPasswordError
from app.security import verify_password
from app.api.models.user import User

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

    user = users_repo.get_by_email(db=db, email=email)

    if not user:
        raise EntityNotFoundError("user does not exist")
    if not verify_password(password, user.password):
        raise BadPasswordError("users password is not correct")

    access_token = create_access_token(
            token_type="access_token",
            lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            sub=user.id
        )
    
    return LoginResponse(
        user=User.from_orm(user),
        refresh_token="",
        access_token=access_token,
    )


def create_access_token(
    token_type: str,
    lifetime: timedelta,
    sub: str,
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)