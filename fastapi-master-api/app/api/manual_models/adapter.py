from typing import Union

from app.api.manual_models.bearer_token_adapter_manual import BearerTokenAdapterManual
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Adapter(BaseModel):
    __root__: Annotated[
        Union[BearerTokenAdapterManual],
        Field(discriminator="authorization_type"),
    ]
