from datetime import datetime
from typing import Literal, Union

from pydantic import BaseModel, Field


class CreateAdapterBase(BaseModel):
    user_id: int
    adapter_name: str
    cron_expression: str


class CreateBearerTokenAdapter(CreateAdapterBase):
    authorization_type: Literal["bearer_token"]
    bearer_token: str


class CreateApiKeyAdapter(CreateAdapterBase):
    authorization_type: Literal["api_key"]
    api_key: str


class CreateAdapter(BaseModel):
    __root__: Union[CreateBearerTokenAdapter, CreateApiKeyAdapter] = Field(
        ..., discriminator="authorization_type"
    )


class Adapter(BaseModel):
    id: int
    user_id: int
    adapter_name: str
    cron_expression: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
