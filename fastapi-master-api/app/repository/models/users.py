from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import column_property, relationship

from .base import BaseModel as Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )
    last_login = Column(DateTime(True))
    date_joined = Column(DateTime(True), nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String(128), nullable=False)