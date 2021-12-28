from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateUser(BaseModel):
    is_superuser: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    password: str


class UpdateUser(CreateUser):
    is_superuser: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class User(CreateUser):
    id: int
    last_login_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
