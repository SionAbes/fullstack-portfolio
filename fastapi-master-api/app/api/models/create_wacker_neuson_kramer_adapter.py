# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.base_create_adapter import BaseCreateAdapter
from app.api.models.base_wacker_neuson_kramer_adapter import (
    BaseWackerNeusonKramerAdapter,
)
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateWackerNeusonKramerAdapter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateWackerNeusonKramerAdapter - a model defined in OpenAPI

        adapter_name: The adapter_name of this CreateWackerNeusonKramerAdapter.
        data_url: The data_url of this CreateWackerNeusonKramerAdapter.
        cron_expression: The cron_expression of this CreateWackerNeusonKramerAdapter.
        token_url: The token_url of this CreateWackerNeusonKramerAdapter.
        username: The username of this CreateWackerNeusonKramerAdapter.
        password: The password of this CreateWackerNeusonKramerAdapter.
        client_id: The client_id of this CreateWackerNeusonKramerAdapter.
        client_secret: The client_secret of this CreateWackerNeusonKramerAdapter.
    """

    adapter_name: str
    data_url: str
    cron_expression: str
    token_url: str
    username: str
    password: str
    client_id: str
    client_secret: str


CreateWackerNeusonKramerAdapter.update_forward_refs()
