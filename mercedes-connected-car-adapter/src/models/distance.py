from datetime import datetime

from pydantic import BaseModel
from src.models.shared import RetrievalStatus


class DistanceDriven(BaseModel):
    unit: str
    value: float
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Distance(BaseModel):
    odometer: DistanceDriven
    distancesincereset: DistanceDriven
    distancesincestart: DistanceDriven
