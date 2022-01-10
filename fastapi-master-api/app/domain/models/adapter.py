import os
from datetime import datetime
from typing import Literal, Union

from app.dependancies import decrypt_string
from app.settings import get_settings
from pydantic import BaseModel, Field, validator
from typing_extensions import Annotated


class CreateAdapterBase(BaseModel):
    user_id: int
    adapter_name: str
    cron_expression: str


class CreateBearerTokenAdapter(CreateAdapterBase):
    authorization_type: Literal["bearer_token"]
    bearer_token: str

    @validator("bearer_token", pre=True)
    def decrypt(value, field):
        settings = get_settings()
        decrypt_string(string_to_decrypt=value, secret=settings.HASH_SECRET)
        return value


class CreateApiKeyAdapter(CreateAdapterBase):
    authorization_type: Literal["api_key"]
    api_key: str

    @validator("api_key", pre=True)
    def decrypt(value, field):
        settings = get_settings()
        decrypt_string(string_to_decrypt=value, secret=settings.HASH_SECRET)
        return value


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

    @validator("bearer_token", pre=True)
    def decrypt(value, field):
        settings = get_settings()
        decrypt_string(string_to_decrypt=value, secret=settings.HASH_SECRET)
        return value


class ApiKeyAdapter(AdapterBase):
    authorization_type: Literal["api_key"]
    api_key: str

    @validator("api_key", pre=True)
    def decrypt(value, field):
        settings = get_settings()
        decrypt_string(string_to_decrypt=value, secret=settings.HASH_SECRET)
        return value


class Adapter(BaseModel):
    __root__: Annotated[
        Union[BearerTokenAdapter, ApiKeyAdapter],
        Field(discriminator="authorization_type"),
    ]
