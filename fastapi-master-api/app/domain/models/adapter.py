from datetime import datetime
from typing import Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated


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


class AdapterBase(BaseModel):
    id: int
    user_id: int
    adapter_name: str
    cron_expression: str
    created_at: datetime
    updated_at: datetime


class BearerTokenAdapter(AdapterBase):
    authorization_type: Literal["bearer_token"]
    bearer_token: str


class ApiKeyAdapter(AdapterBase):
    authorization_type: Literal["api_key"]
    api_key: str


class Adapter(BaseModel):
    __root__: Annotated[
        Union[BearerTokenAdapter, ApiKeyAdapter],
        Field(discriminator="authorization_type"),
    ]
