from app.api.models.user import User as UserSchema
from app.repository.database.crud import CRUDBase
from app.repository.models.users import User
from sqlalchemy.orm import Session
from typing import Optional
from app.security import get_password_hash


class UsersRepo(CRUDBase[User, UserSchema, UserSchema]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserSchema) -> User:
        create_data = obj_in.dict()
        create_data.pop("password")
        db_obj = User(**create_data)
        db_obj.hashed_password = get_password_hash(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

users_repo = UsersRepo(User)
