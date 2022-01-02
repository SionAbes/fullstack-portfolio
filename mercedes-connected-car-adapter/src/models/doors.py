from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from src.models.shared import RetrievalStatus


class DoorOpenValue(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class DoorLockValue(Enum):
    LOCKED = "LOCKED"
    UNLOCKED = "UNLOCKED"


class DoorOpenStatus(BaseModel):
    value: DoorOpenValue
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class DoorLockStatus(BaseModel):
    value: DoorLockValue
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Doors(BaseModel):
    doorstatusfrontleft: Optional[DoorOpenStatus]
    doorstatusfrontright: Optional[DoorOpenStatus]
    doorstatusrearleft: Optional[DoorOpenStatus]
    doorstatusrearright: Optional[DoorOpenStatus]
    doorlockstatusfrontleft: Optional[DoorLockStatus]
    doorlockstatusfrontright: Optional[DoorLockStatus]
    doorlockstatusrearleft: Optional[DoorLockStatus]
    doorlockstatusrearright: Optional[DoorLockStatus]
    doorlockstatusdecklit: Optional[DoorLockStatus]
    doorlockstatusgas: Optional[DoorLockStatus]
    doorlockstatusvehicle: Optional[DoorLockStatus]
