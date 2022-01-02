import enum

from app.repository.models.users import User
from sqlalchemy import Column, Enum, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import BaseModel, TimesMixin


class AdapterEnums(enum.Enum):
    mercedes_connected_car = "mercedes_connected_car"


class Adapter(TimesMixin, BaseModel):
    __tablename__ = "adapters"

    id = Column(
        Integer,
        primary_key=True,
    )
    user_id = Column(
        ForeignKey(User.id, deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    user = relationship("User")
    cron_expression = Column(Text)
    adapter_name = Column(Enum(AdapterEnums))

    __table_args__ = (UniqueConstraint(user_id, adapter_name),)
