from datetime import datetime
from typing import Optional

from app.domain.machine import CreateMachine
from pydantic import BaseModel


class CreateMetric(BaseModel):
    user_id: int
    processed_at: Optional[datetime] = None
    event_at: Optional[datetime] = None
    machine: Optional[CreateMachine] = None
    oem: Optional[str] = None
    metric: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None


class Metric(CreateMetric):
    id: int
    user_id: int
    created_at: datetime
