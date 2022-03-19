# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateMachine(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateMachine - a model defined in OpenAPI

        user_id: The user_id of this CreateMachine.
        unit_installed_at: The unit_installed_at of this CreateMachine [Optional].
        oem_name: The oem_name of this CreateMachine.
        model: The model of this CreateMachine.
        make: The make of this CreateMachine [Optional].
        equipment_id: The equipment_id of this CreateMachine [Optional].
        serial_number: The serial_number of this CreateMachine [Optional].
        pin: The pin of this CreateMachine [Optional].
    """

    user_id: int
    unit_installed_at: Optional[datetime] = None
    oem_name: str
    model: str
    make: Optional[str] = None
    equipment_id: Optional[str] = None
    serial_number: Optional[str] = None
    pin: Optional[str] = None


CreateMachine.update_forward_refs()
