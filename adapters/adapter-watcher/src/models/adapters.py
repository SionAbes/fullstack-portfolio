from datetime import datetime

from app.api.models.adapter_enums import AdapterEnums
from pydantic import BaseModel


class Adapter(BaseModel):

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    adapter_name: str
    cron_expression: str
