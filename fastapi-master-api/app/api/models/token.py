# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Token(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Token - a model defined in OpenAPI

        refresh_token: The refresh_token of this Token.
        access_token: The access_token of this Token.
    """

    refresh_token: str
    access_token: str

Token.update_forward_refs()
