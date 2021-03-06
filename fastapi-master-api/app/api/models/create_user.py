# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class CreateUser(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateUser - a model defined in OpenAPI

        is_superuser: The is_superuser of this CreateUser.
        first_name: The first_name of this CreateUser [Optional].
        last_name: The last_name of this CreateUser [Optional].
        email: The email of this CreateUser.
        password: The password of this CreateUser.
    """

    is_superuser: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    password: str


CreateUser.update_forward_refs()
