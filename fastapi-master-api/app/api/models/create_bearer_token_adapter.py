# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.adapter_enums import AdapterEnums
from app.api.models.base_create_adapter import BaseCreateAdapter
from app.api.models.bearer_token import BearerToken
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateBearerTokenAdapter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateBearerTokenAdapter - a model defined in OpenAPI

        adapter_name: The adapter_name of this CreateBearerTokenAdapter.
        cron_expression: The cron_expression of this CreateBearerTokenAdapter.
        authorization_type: The authorization_type of this CreateBearerTokenAdapter.
        bearer_token: The bearer_token of this CreateBearerTokenAdapter.
    """

    adapter_name: AdapterEnums
    cron_expression: str
    authorization_type: str
    bearer_token: str


CreateBearerTokenAdapter.update_forward_refs()
