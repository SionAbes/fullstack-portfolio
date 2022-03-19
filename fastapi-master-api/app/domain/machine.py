from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateMachine(BaseModel):
    user_id: int
    unit_installed_at: Optional[datetime] = None
    oem_name: str
    model: str
    make: Optional[str] = None
    equipment_id: Optional[str] = None
    serial_number: Optional[str] = None
    pin: Optional[str] = None


class UpdateMachine(CreateMachine):
    pass


class Machine(UpdateMachine):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
