# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from app.api.models.create_machine import CreateMachine
from app.api.models.create_metric import CreateMetric
from app.api.models.created_metric_base import CreatedMetricBase
from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Metric(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Metric - a model defined in OpenAPI

        processed_at: The processed_at of this Metric [Optional].
        event_at: The event_at of this Metric [Optional].
        machine: The machine of this Metric [Optional].
        oem: The oem of this Metric [Optional].
        metric: The metric of this Metric [Optional].
        value: The value of this Metric [Optional].
        unit: The unit of this Metric [Optional].
        machine_id: The machine_id of this Metric.
        user_id: The user_id of this Metric.
        created_at: The created_at of this Metric.
    """

    processed_at: Optional[datetime] = None
    event_at: Optional[datetime] = None
    machine: Optional[CreateMachine] = None
    oem: Optional[str] = None
    metric: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None
    machine_id: int
    user_id: int
    created_at: datetime


Metric.update_forward_refs()
