from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreateUser(BaseModel):
    is_superuser: bool
    first_name: str
    last_name: str
    email: str
    password: str


class User(CreateUser):
    id: int
    last_login_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
