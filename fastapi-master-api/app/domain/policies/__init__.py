from .base import Policy
from .machine import MachinePolicy

POLICIES_REGISTRY: dict[str, Policy] = {"Machine": MachinePolicy}
