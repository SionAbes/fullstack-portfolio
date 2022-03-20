import datetime

from app.repository.models.machines import Machine
from app.repository.models.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import backref, relationship

from .base import BaseModel, TimesMixin


class Metric(TimesMixin, BaseModel):
    __tablename__ = "metrics"
    user_id = Column(
        ForeignKey(User.id, deferrable=True, initially="DEFERRED"),
        nullable=True,
        index=True,
    )
    user = relationship(
        "User",
        backref=backref("metric", lazy="subquery"),
    )
    created_at = Column(DateTime(True), nullable=False, default=datetime.datetime.now)
    processed_at = Column(
        DateTime(timezone=True),
        nullable=False,
    )
    event_at = Column(DateTime(timezone=True), nullable=False, primary_key=True)
    machine_id = Column(
        ForeignKey(Machine.id, deferrable=True, initially="DEFERRED"),
        nullable=True,
        primary_key=True,
    )
    machine = relationship(
        "Machine",
        backref=backref("metric", lazy="subquery"),
    )
    metric = Column(Text, primary_key=True)
    value = Column(Text)
    unit = Column(Text)
