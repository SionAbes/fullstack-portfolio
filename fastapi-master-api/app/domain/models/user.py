from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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
