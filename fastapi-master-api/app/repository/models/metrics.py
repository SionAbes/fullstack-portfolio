import datetime

from app.repository.models.machines import Machine
from app.repository.models.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import backref, relationship

from .base import BaseModel, TimesMixin


class Metric(TimesMixin, BaseModel):
    __tablename__ = "metrics"
    id = Column(
        Integer,
        primary_key=True,
    )
