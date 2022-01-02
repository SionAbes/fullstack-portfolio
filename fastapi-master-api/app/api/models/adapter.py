# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.adapter_enums import AdapterEnums
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Adapter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Adapter - a model defined in OpenAPI

        id: The id of this Adapter.
        user_id: The user_id of this Adapter.
        created_at: The created_at of this Adapter.
        updated_at: The updated_at of this Adapter.
        adapter_name: The adapter_name of this Adapter.
        cron_expression: The cron_expression of this Adapter.
    """

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    adapter_name: AdapterEnums
    cron_expression: str


Adapter.update_forward_refs()
