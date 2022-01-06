import enum
from datetime import datetime

from app.repository.models.users import User
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from .base import BaseModel, TimesMixin


class Adapter(TimesMixin, BaseModel):
    __tablename__ = "adapters"
    __mapper_args__ = {
        "polymorphic_identity": "adapter",
        "polymorphic_on": "authorization_type",
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
    authorization_type = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint(user_id, adapter_name),)


class AuthorizationBearerToken(Adapter):
    __tablename__ = "authorization_bearer_token"
    __mapper_args__ = {"polymorphic_identity": "bearer_token"}

    auth_type_id = Column(
        "id", Integer, ForeignKey(Adapter.id, ondelete="CASCADE"), primary_key=True
    )
    bearer_token = Column(Text, nullable=False)
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
