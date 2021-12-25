from fastapi import APIRouter, Security, Depends
from app.api.models.user import User
from app.api.manual_models.token import TokenModel
from app.security import get_current_user
from app.api.models.create_user import CreateUser
from app.domain.models.user import CreateUser as DomainCreateUser
from app.dependancies import get_db
from sqlalchemy.orm import Session
from app.domain.users import create_user as domain_create_user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_model=User,
    summary="creates a new user",
)
def create_user(
    create_user: CreateUser,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(
        get_current_user, scopes=["ADMIN"]
    ),
) -> User:
    user = domain_create_user(
        create_user=DomainCreateUser(
            is_superuser=create_user.is_superuser,
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            email=create_user.email,
            password=create_user.password,
        ),
        db=db
    )
    return User(
        id=user.id,
        last_login=user.last_login_at,
        date_joined=user.created_at,
        is_superuser=user.is_superuser,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )

