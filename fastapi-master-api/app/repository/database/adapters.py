from typing import List

from app.domain.exceptions import EntityConflictError
from app.domain.models.adapter import Adapter as DomainAdapter
from app.domain.models.adapter import CreateAdapter as DomainCreateAdapter
from app.repository.database.crud import CRUDBase
from app.repository.models.adapters import Adapter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class AdaptersRepo(CRUDBase[Adapter, DomainCreateAdapter, DomainCreateAdapter]):
    def create(self, db: Session, *, obj_in: DomainCreateAdapter) -> DomainAdapter:
        try:
            create_data = obj_in.dict()
            adapter = Adapter(**create_data)
            db.add(adapter)
            db.commit()
        except IntegrityError:
            db.rollback()
            raise EntityConflictError

        return DomainAdapter(
            id=adapter.id,
            user_id=adapter.user_id,
            created_at=adapter.created_at,
            updated_at=adapter.updated_at,
            adapter_name=adapter.adapter_name.value,
            cron_expression=adapter.cron_expression,
        )

    def list(self, db: Session) -> List[DomainAdapter]:
        adapters = db.query(self.model).all()
        return [
            DomainAdapter(
                id=adapter.id,
                user_id=adapter.user_id,
                created_at=adapter.created_at,
                updated_at=adapter.updated_at,
                adapter_name=adapter.adapter_name.value,
                cron_expression=adapter.cron_expression,
            )
            for adapter in adapters
        ]


adapters_repo = AdaptersRepo(Adapter)
