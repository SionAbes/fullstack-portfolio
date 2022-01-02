from datetime import datetime

from pydantic import BaseModel


class Vehicle(BaseModel):
    make: str
    model_year: int
    model: str
    license_plate: str
    vin: str


class VehicleDataPoint(BaseModel):
    unit: str
    value: float
    timestamp: datetime
