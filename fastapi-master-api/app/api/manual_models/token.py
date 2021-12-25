from pydantic import BaseModel
from typing import List

class TokenModel(BaseModel):
    """Defines a token model."""

    type: str
    exp: int
    iat: str
    sub: int
    roles: List[str]
