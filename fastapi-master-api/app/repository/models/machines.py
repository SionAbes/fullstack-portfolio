import datetime

from app.repository.models.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import backref, relationship

from .base import BaseModel, TimesMixin


class Machine(TimesMixin, BaseModel):
    __tablename__ = "machines"

    id = Column(
        Integer,
        primary_key=True,
    )
    user_id = Column(
        ForeignKey(User.id, deferrable=True, initially="DEFERRED"),
        nullable=True,
        index=True,
    )
    user = relationship(
        "User",
        backref=backref("machine", lazy="subquery"),
    )
    created_at = Column(DateTime(True), nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    unit_installed_at = Column(
        DateTime(timezone=True),
    )
    oem_name = Column(
        Text,
        nullable=False,
    )
    model = Column(Text)
    make = Column(Text)
    equipment_id = Column(Text)
    serial_number = Column(Text, primary_key=True)
    pin = Column(Text, primary_key=True)
