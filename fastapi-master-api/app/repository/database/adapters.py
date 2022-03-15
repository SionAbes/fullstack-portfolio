from typing import Generic, List, TypeVar

from app.domain.adapter import Adapter as DomainAdapter
from app.domain.adapter import (
    CreateLiebherrLidatAdapter,
    CreateTakeuchiTfmAdapter,
    CreateVolvoCaretrackAdapter,
    CreateWackerNeusonKramerAdapter,
)
from app.repository.models.adapters import (
    Adapter,
    AdapterLiebherrLidat,
    AdapterTakeuchiTfm,
    AdapterVolvoCaretrack,
    AdapterWackerNeusonKramer,
)
from app.repository.models.base import BaseModel as Base
from app.service.exceptions import EntityConflictError, NotSupportedError
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, with_polymorphic

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class PolymorphicAdaptersBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.adapters = with_polymorphic(
            Adapter, [AdapterWackerNeusonKramer, AdapterVolvoCaretrack]
        )

    def list(self, db: Session) -> List[DomainAdapter]:
        adapters = db.query(self.adapters).all()
        return [DomainAdapter.parse_obj(adapter.__dict__) for adapter in adapters]

    def create(self, db: Session, *, obj_in) -> DomainAdapter:
        model = self._check_instance_model(obj_in)
        if not model:
            raise NotSupportedError(
                f"update_answer of type: {type(obj_in)} is not supported"
            )
        try:
            create_data = obj_in.dict()
            adapter = model(**create_data)
            db.add(adapter)
            db.flush()
        except IntegrityError:
            db.rollback()
            raise EntityConflictError
        return DomainAdapter.parse_obj(adapter.__dict__)

    def _check_instance_model(self, domain_model):
        if isinstance(domain_model, CreateWackerNeusonKramerAdapter):
            return AdapterWackerNeusonKramer
        if isinstance(domain_model, CreateVolvoCaretrackAdapter):
            return AdapterVolvoCaretrack
        if isinstance(domain_model, CreateLiebherrLidatAdapter):
            return AdapterLiebherrLidat
        if isinstance(domain_model, CreateTakeuchiTfmAdapter):
            return AdapterTakeuchiTfm


adapters_repo = PolymorphicAdaptersBase()
