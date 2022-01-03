from typing import List

from app.api.exceptions import HTTP409Exception
from app.api.manual_models.adapter import AdapterManual as Adapter
from app.api.manual_models.create_adapter import CreateAdapterManual as CreateAdapter
from app.api.manual_models.token import TokenModel
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
    response_model=Adapter,
    summary="creates a new adapter instance",
)
def create_adapter(
    create_adapter: CreateAdapter,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> Adapter:
    try:
        adapter = domain_create_adapter(
            db=db,
            create_adapter=DomainCreateAdapter(
                user_id=token_user.sub,
                adapter_name=create_adapter.adapter_name.value,
                cron_expression=create_adapter.cron_expression,
            ),
        )
    except EntityConflictError:
        raise HTTP409Exception
    return Adapter(
        id=adapter.id,
        user_id=adapter.user_id,
        created_at=adapter.created_at,
        updated_at=adapter.updated_at,
        adapter_name=adapter.adapter_name,
        cron_expression=adapter.cron_expression,
    )


@router.get(
    "/",
    summary="a list of adapter instances",
    response_model=List[Adapter],
)
def fetch_adapters(
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN"]),
) -> List[Adapter]:
    adapters = domain_fetch_adapters(db=db)
    return [
        Adapter(
            id=adapter.id,
            user_id=adapter.user_id,
            created_at=adapter.created_at,
            updated_at=adapter.updated_at,
            adapter_name=adapter.adapter_name,
            cron_expression=adapter.cron_expression,
        )
        for adapter in adapters
    ]
