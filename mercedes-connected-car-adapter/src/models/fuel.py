from datetime import datetime

from pydantic import BaseModel
from src.models.shared import RetrievalStatus


class FuelStatus(BaseModel):
    unit: str
    value: float
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Fuel(BaseModel):
    fuellevelpercent: FuelStatus
