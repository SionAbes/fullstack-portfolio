from app.domain.user_token import LoggedUser
from app.service.exceptions import EntityNotFoundError
from sqlalchemy.orm import Session

from .base import Policy


class MachinePolicy(Policy):
    def __init__(
        self,
        subject: LoggedUser,
        machine_id: int,
        db: Session,
        options: dict = {},
    ):
        self.db = db
        self.subject = subject
        self.machine_id = machine_id
        self.options = options

    def list(self) -> bool:
        return True
