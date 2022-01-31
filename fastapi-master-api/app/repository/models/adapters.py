from datetime import datetime

from app.repository.models.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import BaseModel, TimesMixin


class Adapter(TimesMixin, BaseModel):
    __tablename__ = "adapters"
    __mapper_args__ = {
        "polymorphic_identity": "adapter",
        "polymorphic_on": "adapter_name",
    }

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
    adapter_name = Column(Text)
    data_url = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint(user_id, adapter_name),)


class AdapterWackerNeusonKramer(Adapter):
    __tablename__ = "adapter_wacker_neuson_kramer"
    __mapper_args__ = {"polymorphic_identity": "wacker_neuson_kramer"}

    adapter_id = Column(
        "id", Integer, ForeignKey(Adapter.id, ondelete="CASCADE"), primary_key=True
    )
    token_url = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    client_id = Column(Text, nullable=False)
    client_secret = Column(Text, nullable=False)
    child_created_at = Column(
        "created_at", DateTime(True), nullable=False, default=datetime.now()
    )
    child_updated_at = Column(
        "updated_at",
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
    )


class AdapterVolvoCaretrack(Adapter):
    __tablename__ = "adapter_volvo_caretrack"
    __mapper_args__ = {"polymorphic_identity": "volvo_caretrack"}

    adapter_id = Column(
        "id", Integer, ForeignKey(Adapter.id, ondelete="CASCADE"), primary_key=True
    )
    password = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    child_created_at = Column(
        "created_at", DateTime(True), nullable=False, default=datetime.now()
    )
    child_updated_at = Column(
        "updated_at",
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
    )
