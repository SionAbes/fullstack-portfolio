from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Machine(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    unit_installed_at: Optional[datetime] = None
    oem_name: str
    model: Optional[str] = None
    make: Optional[str] = None
    equipment_id: Optional[str] = None
    serial_number: Optional[str] = None
    pin: Optional[str] = None

    class Config:
        orm_mode = True
