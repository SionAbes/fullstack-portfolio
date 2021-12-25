from app.domain.models.user import User as UserDomain
from app.repository.database.crud import CRUDBase
from app.repository.models.users import User
from sqlalchemy.orm import Session
from typing import Optional
from app.security import get_password_hash
from datetime import datetime

class UsersRepo(CRUDBase[User, UserDomain, UserDomain]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserDomain]:
        user = db.query(User).filter(User.email == email).first()
        if user:
            user.last_login_at = datetime.utcnow()
            self.update(db=db, obj_in=user.__dict__, id=user.id)
        return UserDomain(
            id=user.id,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )

    def create(self, db: Session, *, obj_in: UserDomain) -> UserDomain:
        create_data = obj_in.dict()
        create_data.pop("password")
        user = User(**create_data)
        if user:
            user.last_login_at = datetime.utcnow()
        user.password = get_password_hash(obj_in.password)
        db.add(user)
        db.commit()

        return UserDomain(
            id=user.id,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )


users_repo = UsersRepo(User)
