from datetime import datetime
from typing import Literal, Union

from app.security import get_string_hash
from pydantic import BaseModel, Field, validator


class CreateAdapterBase(BaseModel):
    data_url: str
    cron_expression: str
    user_id: int


class CreateVolvoCaretrackAdapter(CreateAdapterBase):
    adapter_name: Literal["volvo_caretrack"]
    username: str
    password: str

    @validator("password")
    def hash_password(cls, pw: str) -> str:
        return get_string_hash(pw)


class CreateWackerNeusonKramerAdapter(CreateAdapterBase):
    adapter_name: Literal["wacker_neuson_kramer"]
    token_url: str
    username: str
    password: str
    client_id: str
    client_secret: str

    @validator("password")
    def hash_password(cls, pw: str) -> str:
        return get_string_hash(pw)

    @validator("client_id")
    def hash_client_id(cls, cid: str) -> str:
        return get_string_hash(cid)

    @validator("client_secret")
    def hash_client_secret(cls, cs: str) -> str:
        return get_string_hash(cs)


class CreateLiebherrLidatAdapter(CreateAdapterBase):
    adapter_name: Literal["liebherr_lidat"]
    username: str
    password: str

    @validator("password")
    def hash_password(cls, pw: str) -> str:
        return get_string_hash(pw)


class CreateTakeuchiTfmAdapter(CreateAdapterBase):
    adapter_name: Literal["takeuchi_tfm"]
    token_url: str
    client_id: str
    client_secret: str

    @validator("client_id")
    def hash_client_id(cls, cid: str) -> str:
        return get_string_hash(cid)

    @validator("client_secret")
    def hash_client_secret(cls, cs: str) -> str:
        return get_string_hash(cs)


class CreateAdapter(BaseModel):
    __root__: Union[
        CreateVolvoCaretrackAdapter,
        CreateLiebherrLidatAdapter,
        CreateWackerNeusonKramerAdapter,
        CreateTakeuchiTfmAdapter,
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


class LiebherrLidatAdapter(AdapterBase):
    adapter_name: Literal["liebherr_lidat"]
    username: str
    password: str


class TakeuchiTfmAdapter(AdapterBase):
    adapter_name: Literal["takeuchi_tfm"]
    token_url: str
    client_id: str
    client_secret: str


class Adapter(BaseModel):
    __root__: Union[
        WackerNeusonKramerAdapter,
        VolvoCaretrackAdapter,
        LiebherrLidatAdapter,
        TakeuchiTfmAdapter,
    ] = Field(..., discriminator="adapter_name")
