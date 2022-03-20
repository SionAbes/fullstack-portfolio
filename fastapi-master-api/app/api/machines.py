from typing import List

from app.api.exceptions import not_authorized_handler
from app.api.manual_models.token import TokenModel
from app.api.models.create_machine import CreateMachine
from app.api.models.machine import Machine
from app.dependancies import get_db
from app.domain import machine as domain
from app.domain.user_token import LoggedUser
from app.security import get_current_user
from app.service import machines as service
from app.service.authorization import NotAuthorizedError
from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/machines",
    tags=["Machines"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[Machine],
    response_model_exclude_none=True,
)
def fetch_machines(
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN", "USER"]),
) -> List[Machine]:
    token = LoggedUser(token_user)
    machines = service.FetchMachines(
        db=db,
        token=token,
    ).list()
    return [_build_api_model(machine) for machine in machines]


@router.post(
    "/",
    summary="creates a new machine",
    response_model=Machine,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
def create_machine(
    create_machine: CreateMachine,
    db: Session = Depends(get_db),
    token_user: TokenModel = Security(get_current_user, scopes=["ADMIN", "USER"]),
) -> Machine:
    token = LoggedUser(token_user)
    try:
        domain_create_machine = domain.CreateMachine(**create_machine.dict())
        domain_create_machine.user_id = token.id
        machine = service.CreateMachine(
            db=db,
            create_machine=domain_create_machine,
            token=token,
        ).create()
    except NotAuthorizedError as error:
        return not_authorized_handler(error)
    return _build_api_model(machine)


def _build_api_model(domain_model: domain.Machine) -> Machine:
    return Machine(**domain_model.dict())
