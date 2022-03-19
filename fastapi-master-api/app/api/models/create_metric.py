# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.create_machine import CreateMachine
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateMetric(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateMetric - a model defined in OpenAPI

        processed_at: The processed_at of this CreateMetric [Optional].
        event_at: The event_at of this CreateMetric [Optional].
        machine: The machine of this CreateMetric [Optional].
        oem: The oem of this CreateMetric [Optional].
        metric: The metric of this CreateMetric [Optional].
        value: The value of this CreateMetric [Optional].
        unit: The unit of this CreateMetric [Optional].
    """

    processed_at: Optional[datetime] = None
    event_at: Optional[datetime] = None
    machine: Optional[CreateMachine] = None
    oem: Optional[str] = None
    metric: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None


CreateMetric.update_forward_refs()
