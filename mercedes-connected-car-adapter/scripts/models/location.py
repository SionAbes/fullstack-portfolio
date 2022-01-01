from datetime import datetime

from pydantic import BaseModel
from scripts.models.shared import RetrievalStatus


class LocationCoordinate(BaseModel):
    value: float
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Location(BaseModel):
    latitude: LocationCoordinate
    longitude: LocationCoordinate
    heading: LocationCoordinate
