from datetime import datetime

from pydantic import BaseModel


class CreateAdapter(BaseModel):
    user_id: int
    adapter_name: str
    cron_expression: str


class Adapter(CreateAdapter):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
