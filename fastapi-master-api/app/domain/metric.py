from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateMetric(BaseModel):
    machine_id: int
    user_id: Optional[int]
    processed_at: Optional[datetime] = None
    event_at: Optional[datetime] = None
    machine_id: int
    metric: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None


class UpdateMetric(CreateMetric):
    pass


class Metric(CreateMetric):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
