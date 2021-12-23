from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .base import TimesMixin, BaseModel


class User(TimesMixin, BaseModel):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )
    last_login = Column(DateTime(True))
    is_superuser = Column(Boolean, nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String(128), nullable=False)

