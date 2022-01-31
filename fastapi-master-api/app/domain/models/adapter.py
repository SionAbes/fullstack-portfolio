from datetime import datetime
from typing import Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class CreateAdapterBase(BaseModel):
    data_url: str
    cron_expression: str
    user_id: int


class CreateVolvoCaretrackAdapter(CreateAdapterBase):
    adapter_name: Literal["volvo_caretrack"]
    username: str
    password: str


class CreateWackerNeusonKramerAdapter(CreateAdapterBase):
    adapter_name: Literal["wacker_neuson_kramer"]
    token_url: str
    username: str
    password: str
    client_id: str
    client_secret: str


class CreateAdapter(BaseModel):
    __root__: Union[
        CreateVolvoCaretrackAdapter, CreateWackerNeusonKramerAdapter
    ] = Field(..., discriminator="adapter_name")


class AdapterBase(BaseModel):
    id: int
    user_id: int
    adapter_name: str
    cron_expression: str
    data_url: str
    created_at: datetime
    updated_at: datetime


class VolvoCaretrackAdapter(AdapterBase):
    adapter_name: Literal["volvo_caretrack"]
    username: str
    password: str


class WackerNeusonKramerAdapter(AdapterBase):
    adapter_name: Literal["wacker_neuson_kramer"]
    token_url: str
    username: str
    password: str
    client_id: str
    client_secret: str


class Adapter(BaseModel):
    __root__: Union[VolvoCaretrackAdapter, WackerNeusonKramerAdapter] = Field(
        ..., discriminator="adapter_name"
    )
