from datetime import datetime
from typing import Optional

from app.domain.models.user import CreateUser as DomainCreateUser
from app.domain.models.user import UpdateUser as DomainUpdateUser
from app.domain.models.user import User as DomainUser
from app.repository.database.crud import CRUDBase
from app.repository.models.users import User
from app.security import get_password_hash
from sqlalchemy.orm import Session


class UsersRepo(CRUDBase[User, DomainCreateUser, DomainUpdateUser]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[DomainUser]:
        query = db.query(self.db_model).filter(User.email == email)
        db_obj = self._filter_soft_deleted(query).first()
        if not db_obj:
            return None
        return self._create_object(db_obj=db_obj)

    def create(self, db: Session, *, obj_in: DomainCreateUser) -> DomainUser:
        create_data = obj_in.dict()
        create_data.pop("password")
        user = self.db_model(**create_data)
        if user:
            user.last_login_at = datetime.utcnow()
        user.password = get_password_hash(obj_in.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return self._create_object(db_obj=user)


users_repo = UsersRepo(db_model=User, domain_model=DomainUser)
