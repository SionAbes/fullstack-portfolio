from typing import List

from app.api.manual_models.token import TokenModel
from app.api.models.create_user import CreateUser
from app.api.models.update_user import UpdateUser
from app.api.models.user import User
from app.dependancies import get_db
from app.domain.models.user import CreateUser as DomainCreateUser
from app.domain.users import create_user as domain_create_user
from app.domain.users import fetch_users as domain_fetch_users
from app.security import get_current_user
from fastapi import APIRouter, Depends, HTTPException, Response, Security, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
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
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> User:
    user = domain_create_user(
        create_user=DomainCreateUser(
            is_superuser=create_user.is_superuser,
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            email=create_user.email,
            password=create_user.password,
        ),
        db=db,
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


@router.get(
    "/",
    summary="a list of the requested users",
    response_model=List[User],
)
def fetch_users(
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> List[User]:
    users = domain_fetch_users(db=db)
    return [
        User(
            id=user.id,
            last_login=user.last_login_at,
            date_joined=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )
        for user in users
    ]


@router.put(
    "/{id}/",
    summary="updates a users information by its id",
    response_model=User,
)
def update_user_by_id(
    id: int,
    update_user: UpdateUser,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> User:
    try:
        return service_update_user_by_id(
            user_id=id,
            update_answer=update_user,
            db=db,
        )
    except NoEntryFoundException:
        raise HTTP404Exception()
    except NotAuthorizedError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to access this operation",
        )


@router.delete(
    "/{id}/",
    summary="deletes a users by its id",
)
def delete_user_by_id(
    id: int,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
):
    try:
        success_flag = service_delete_user_by_id(user_id=id, db=db)
        if not success_flag:
            raise HTTP404Exception()

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except NotAuthorizedError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to access this operation",
        )
