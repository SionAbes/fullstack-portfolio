from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .base import BaseModel, TimesMixin


class User(TimesMixin, BaseModel):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )
    last_login_at = Column(DateTime(True))
    is_superuser = Column(Boolean, nullable=False)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=True)
    email = Column(String, index=True, nullable=False)
    password = Column(String(128), nullable=False)
