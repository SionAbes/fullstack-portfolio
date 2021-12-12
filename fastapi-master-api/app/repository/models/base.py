import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class TimesMixin:
    __abstract__ = True

    created_at = Column(DateTime(True), nullable=False, default=datetime.datetime.now())
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
    )
