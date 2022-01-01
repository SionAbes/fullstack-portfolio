from datetime import datetime

from pydantic import BaseModel
from scripts.models.shared import RetrievalStatus


class TirePressureStatus(BaseModel):
    unit: str
    value: float
    retrievalstatus: RetrievalStatus
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class Tires(BaseModel):
    tirepressurefrontleft: TirePressureStatus
    tirepressurefrontright: TirePressureStatus
    tirepressurerearleft: TirePressureStatus
    tirepressurerearright: TirePressureStatus
