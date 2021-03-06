# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreatedMetricBase(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreatedMetricBase - a model defined in OpenAPI

        user_id: The user_id of this CreatedMetricBase.
        created_at: The created_at of this CreatedMetricBase.
    """

    user_id: int
    created_at: datetime


CreatedMetricBase.update_forward_refs()
