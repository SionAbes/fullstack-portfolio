from sqlalchemy.orm import Session
from app.domain.models.user import CreateUser, User
from app.repository.database.users import users_repo
from typing import List


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
