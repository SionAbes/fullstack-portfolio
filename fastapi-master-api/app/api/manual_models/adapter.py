from typing import Union

from app.api.models.liebherr_lidat_adapter import LiebherrLidatAdapter
from app.api.models.takeuchi_tfm_adapter import TakeuchiTfmAdapter
from app.api.models.volvo_caretrack_adapter import VolvoCaretrackAdapter
from app.api.models.wacker_neuson_kramer_adapter import WackerNeusonKramerAdapter
from pydantic import BaseModel, Field


class Adapter(BaseModel):
    __root__: Union[
        WackerNeusonKramerAdapter,
        TakeuchiTfmAdapter,
        VolvoCaretrackAdapter,
        LiebherrLidatAdapter,
    ] = Field(..., discriminator="adapter_name")
