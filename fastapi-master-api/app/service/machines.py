from typing import List

from app.domain import machine as domain
from app.domain.user_token import LoggedUser
from app.repository.database.machines import MachinesRepo, machines_repo
from app.service.authorization import authorize
from sqlalchemy.orm import Session


class FetchMachines:
    def __init__(
        self,
        db: Session,
        token: LoggedUser,
        machine: domain.Machine = domain.Machine,
        machine_repo: MachinesRepo = machines_repo,
    ):
        self.db = db
        self.token = token
        self.machine = machine
        self.machine_repo = machine_repo

    def list(self) -> List[domain.Machine]:
        self._authorize()
        return self._list()

    def _list(self) -> List[domain.Machine]:
        if self.token.is_admin():
            return self.machine_repo.list(self.db)
        return self.machine_repo.list_by(self.db, self.options)

    def _authorize(self):
        self.options = self._build_options()
        authorize(
            self.token,
            self.machine,
            "list",
            self.db,
            self.options,
        )

    def _build_options(self):
        return {"user_id": self.token.id}
