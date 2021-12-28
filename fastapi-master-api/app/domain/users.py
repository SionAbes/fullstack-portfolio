from typing import List

from app.domain.models.user import CreateUser, UpdateUser, User
from app.repository.database.users import users_repo
from sqlalchemy.orm import Session


def create_user(
    create_user: CreateUser,
    db: Session,
) -> User:
    return users_repo.create(db=db, obj_in=create_user)


def fetch_users(
    *,
    db: Session,
) -> List[User]:
    users = users_repo.list(db=db)
    return users


def update_user_by_id(
    *,
    user_id: int,
    update_user: UpdateUser,
    db: Session,
) -> User:
    user = users_repo.update(
        db=db,
        id=user_id,
        obj_in=update_user,
    )
    return user


def delete_user_by_id(
    *,
    user_id: int,
    db: Session,
):

    return users_repo.remove(
        db=db,
        id=user_id,
    )
