from typing import List

from app.api.exceptions import not_authorized_handler
from app.api.manual_models.token import TokenModel
from app.api.models.create_metric import CreateMetric
from app.api.models.metric import Metric
from app.dependancies import get_db
from app.domain import metric as domain
from app.domain.user_token import LoggedUser
from app.security import get_current_user
from app.service import metrics as service
from app.service.authorization import NotAuthorizedError
from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post(
    "/",
    summary="creates a new metric",
    response_model=Metric,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create_metric(
    create_metric: CreateMetric,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN", "USER"]),
) -> Metric:
    token = LoggedUser(token_user)
    try:
        domain_create_metric = domain.CreateMetric(**create_metric.dict())
        domain_create_metric.user_id = token.id
        metric = service.CreateMetric(
            db=db,
            create_metric=domain_create_metric,
            token=token,
        ).create()
    except NotAuthorizedError as error:
        return not_authorized_handler(error)
    return _build_api_model(metric)


def _build_api_model(domain_model: domain.Metric) -> Metric:
    return Metric(**domain_model.dict())
