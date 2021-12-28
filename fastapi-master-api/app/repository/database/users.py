from datetime import datetime
from typing import Optional

from app.domain.models.user import CreateUser as DomainCreateUser
from app.domain.models.user import UpdateUser as DomainUpdateUser
from app.domain.models.user import User as DomainUser
from app.repository.database.crud import CRUDBase
from app.repository.models.users import User
from app.security import get_password_hash
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class UsersRepo(CRUDBase[User, DomainCreateUser, DomainUpdateUser]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[DomainUser]:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if user:
            user.last_login_at = datetime.utcnow()
            self.update(db=db, obj_in=user.__dict__, id=user.id)
        return DomainUser(
            id=user.id,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )

    def create(self, db: Session, *, obj_in: DomainCreateUser) -> DomainUser:
        create_data = obj_in.dict()
        create_data.pop("password")
        user = User(**create_data)
        if user:
            user.last_login_at = datetime.utcnow()
        user.password = get_password_hash(obj_in.password)
        db.add(user)
        db.commit()

        return DomainUser(
            id=user.id,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )

    def update(
        self,
        db: Session,
        id: int,
        *,
        obj_in: DomainUpdateUser,
    ) -> DomainUser:
        user = self.get(db=db, id=id)
        obj_data = jsonable_encoder(user)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(user, field, update_data[field])
        db.add(user)
        db.commit()
        db.refresh(user)
        return DomainUser(
            id=user.id,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            is_superuser=user.is_superuser,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )

    def remove(self, db: Session, *, id: int) -> Optional[DomainUser]:
        user = db.query(self.model).get(id)
        db.delete(user)
        db.commit()
        return DomainUser(
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
