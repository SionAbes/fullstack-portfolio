from .base import Policy
from .machine import MachinePolicy
from .metric import MetricPolicy

POLICIES_REGISTRY: dict[str, Policy] = {
    "Machine": MachinePolicy,
    "Metric": MetricPolicy,
}
