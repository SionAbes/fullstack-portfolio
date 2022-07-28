# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.base_adapter import BaseAdapter
from app.api.models.base_liebherr_lidat_adapter import BaseLiebherrLidatAdapter
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class LiebherrLidatAdapter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LiebherrLidatAdapter - a model defined in OpenAPI

        id: The id of this LiebherrLidatAdapter.
        user_id: The user_id of this LiebherrLidatAdapter.
        created_at: The created_at of this LiebherrLidatAdapter.
        updated_at: The updated_at of this LiebherrLidatAdapter.
        adapter_name: The adapter_name of this LiebherrLidatAdapter.
        cron_expression: The cron_expression of this LiebherrLidatAdapter.
        data_url: The data_url of this LiebherrLidatAdapter.
        username: The username of this LiebherrLidatAdapter.
        password: The password of this LiebherrLidatAdapter.
    """

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    adapter_name: str
    cron_expression: str
    data_url: str
    username: str
    password: str


LiebherrLidatAdapter.update_forward_refs()