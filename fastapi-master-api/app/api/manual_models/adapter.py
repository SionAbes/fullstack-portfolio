from typing import Union

from app.api.models.volvo_caretrack_adapter import VolvoCaretrackAdapter
from app.api.models.wacker_neuson_kramer_adapter import WackerNeusonKramerAdapter
from pydantic import BaseModel, Field


class Adapter(BaseModel):
    __root__: Union[WackerNeusonKramerAdapter, VolvoCaretrackAdapter] = Field(
        ..., discriminator="adapter_name"
    )
