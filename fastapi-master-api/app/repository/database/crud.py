from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app.repository.models.base import BaseModel as Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Query, Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
DomainModel = TypeVar("DomainModel", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        db_model: Type[ModelType],
        domain_model: Optional[Type[DomainModel]] = None,
        soft_delete: Optional[bool] = False,
    ):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class

        This class will return a db_obj with the SQLALchemy ORM which is only supported for backwards compatibility
        purposes, or a Pydantic Domain object. All new repos should use a domain return NOT db!
        """
        self.db_model = db_model
        self.domain_model = domain_model
        self.soft_delete = soft_delete

    def get(self, db: Session, id: int) -> Optional[DomainModel]:
        db_obj = self._retrieve(db=db, id=id)
        if not db_obj:
            return None

        return self._create_object(db_obj=db_obj)

    def list(self, db: Session) -> List[DomainModel]:
        query = db.query(self.db_model)
        db_obj = self._filter_soft_deleted(query).all()
        return [self._create_object(db_obj=entry) for entry in db_obj]

    def list_by(self, db: Session, columns) -> List[DomainModel]:
        query = db.query(self.db_model).filter_by(**columns)
        collection = self._filter_soft_deleted(query).all()
        return [self._create_object(entry) for entry in collection]

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> DomainModel:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.db_model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return self._create_object(db_obj=db_obj)

    def update(
        self,
        db: Session,
        id: int,
        *,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> Optional[DomainModel]:
        db_obj = self._retrieve(db=db, id=id)
        if not db_obj:
            return None

        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return self._create_object(db_obj=db_obj)

    def delete(self, db: Session, *, id: int) -> Optional[DomainModel]:
        db_obj = self._retrieve(db=db, id=id)
        if not db_obj:
            return None

        if self.soft_delete:
            db_obj.deleted = datetime.utcnow()
        else:
            db.delete(db_obj)

        db.commit()
        return self._create_object(db_obj=db_obj)

    def _retrieve(self, db: Session, id: int) -> Optional[DomainModel]:
        query = db.query(self.db_model).filter_by(id=id)
        db_obj = self._filter_soft_deleted(query).first()
        if not db_obj:
            return None
        return db_obj

    def _create_object(self, db_obj: Type[ModelType]) -> DomainModel:
        return self.domain_model.from_orm(db_obj)

    def _filter_soft_deleted(self, query: Query) -> Query:
        if self.soft_delete:
            return query.filter_by(deleted=None)
        return query
