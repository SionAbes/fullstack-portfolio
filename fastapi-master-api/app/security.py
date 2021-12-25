from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from app.settings import get_settings, Settings
from fastapi import Depends, HTTPException, status
import jwt
from app.api.manual_models.token import TokenModel
from typing import List

SETTINGS = get_settings()

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl=f"{SETTINGS.API_URL}/auth/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)


async def get_current_user(
    security_scopes: SecurityScopes,
    settings: Settings = Depends(get_settings),
    token: str = Depends(OAUTH2_SCHEME)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        roles: List[str] = payload.get("roles")
        if not list(set(security_scopes.scopes) & set(roles)):
            raise credentials_exception

        return TokenModel(
            type=payload.get("type"),
            exp=payload.get("exp"),
            iat=payload.get("iat"),
            sub=payload.get("sub"),
            roles=payload.get("roles")
        )
    except jwt.PyJWTError:
        raise credentials_exception
