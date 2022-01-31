# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateLiebherrLidatAdapter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateLiebherrLidatAdapter - a model defined in OpenAPI

        adapter_name: The adapter_name of this CreateLiebherrLidatAdapter.
        data_url: The data_url of this CreateLiebherrLidatAdapter.
        cron_expression: The cron_expression of this CreateLiebherrLidatAdapter.
        username: The username of this CreateLiebherrLidatAdapter.
        password: The password of this CreateLiebherrLidatAdapter.
    """

    adapter_name: str
    data_url: str
    cron_expression: str
    username: str
    password: str


CreateLiebherrLidatAdapter.update_forward_refs()