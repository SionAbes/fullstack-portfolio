from app.domain import metric as domain
from app.repository.database.crud import CRUDBase
from app.repository.models.metrics import Metric


class MetricsRepo(CRUDBase[Metric, domain.CreateMetric, domain.UpdateMetric]):
    pass


metrics_repo = MetricsRepo(db_model=Metric, domain_model=domain.Metric)
