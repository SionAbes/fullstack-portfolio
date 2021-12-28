from typing import List

from pydantic import BaseModel


class TokenModel(BaseModel):
    """Defines a token model."""

    type: str
    exp: int
    iat: str
    sub: int
    roles: List[str]
