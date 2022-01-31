from app.api.manual_models.token import TokenModel
from app.api.models.login_response import LoginResponse
from app.api.models.token import Token
from app.dependancies import get_db
from app.domain.auth import authenticate, create_access_and_refresh_token
from app.domain.exceptions import BadPasswordError, EntityNotFoundError
from app.security import get_current_user
from app.settings import Settings, get_settings
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="login a user with credentials",
)
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
    settings: Settings = Depends(get_settings),
) -> LoginResponse:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """
    try:
        return authenticate(
            email=form_data.username,
            password=form_data.password,
            db=db,
            settings=settings,
        )
    except EntityNotFoundError or BadPasswordError:
        raise HTTPException(status_code=404, detail="This user does not exist")
    except BadPasswordError:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


@router.post(
    "/refresh",
    response_model=Token,
    summary="refresh an access token, to extend its lifetime",
)
def refresh(
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN", "USER"]),
    settings: Settings = Depends(get_settings),
) -> Token:
    if token_user.type != "refresh_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_access_and_refresh_token(
        user_id=token_user.sub, roles=token_user.roles, settings=settings
    )
