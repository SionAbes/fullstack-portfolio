from typing import List, Union

from app.api.exceptions import HTTP409Exception
from app.api.manual_models.adapter import Adapter
from app.api.manual_models.token import TokenModel
from app.api.models.create_liebherr_lidat_adapter import CreateLiebherrLidatAdapter
from app.api.models.create_takeuchi_tfm_adapter import CreateTakeuchiTfmAdapter
from app.api.models.create_volvo_caretrack_adapter import CreateVolvoCaretrackAdapter
from app.api.models.create_wacker_neuson_kramer_adapter import (
    CreateWackerNeusonKramerAdapter,
)
from app.dependancies import get_db
from app.domain.adapters import create_adapter as domain_create_adapter
from app.domain.adapters import fetch_adapters as domain_fetch_adapters
from app.domain.exceptions import EntityConflictError
from app.domain.models.adapter import CreateAdapter as DomainCreateAdapter
from app.security import get_current_user
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/adapters",
    tags=["Adapters"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    summary="creates a new adapter instance",
)
def create_adapter(
    create_adapter: Union[
        CreateWackerNeusonKramerAdapter,
        CreateVolvoCaretrackAdapter,
        CreateLiebherrLidatAdapter,
        CreateTakeuchiTfmAdapter,
    ],
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> Adapter:
    try:
        domain_obj = create_adapter.__dict__
        domain_obj["user_id"] = token_user.sub
        adapter = domain_create_adapter(
            db=db,
            create_adapter=DomainCreateAdapter.parse_obj(domain_obj).__root__,
        )
    except EntityConflictError:
        raise HTTP409Exception
    return Adapter.parse_obj(adapter.__dict__)


@router.get(
    "/",
    summary="a list of adapter instances",
)
def fetch_adapters(
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> List[Adapter]:
    adapters = domain_fetch_adapters(db=db)
    return [Adapter.parse_obj(adapter.__dict__) for adapter in adapters]
