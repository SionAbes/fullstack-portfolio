from app.domain import machine as domain
from app.repository.database.crud import CRUDBase
from app.repository.models.machines import Machine


class MachinesRepo(CRUDBase[Machine, domain.CreateMachine, domain.UpdateMachine]):
    pass


machines_repo = MachinesRepo(db_model=Machine, domain_model=domain.Machine)
