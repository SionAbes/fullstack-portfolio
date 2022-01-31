from typing import List, Union

from app.domain.models.adapter import (
    Adapter,
    CreateVolvoCaretrackAdapter,
    CreateWackerNeusonKramerAdapter,
)
from app.repository.database.adapters import adapters_repo
from sqlalchemy.orm import Session


def create_adapter(
    create_adapter: Union[CreateVolvoCaretrackAdapter, CreateWackerNeusonKramerAdapter],
    db: Session,
) -> Adapter:
    return adapters_repo.create(db=db, obj_in=create_adapter)


def fetch_adapters(
    *,
    db: Session,
) -> List[Adapter]:
    adapters = adapters_repo.list(db=db)
    return adapters
