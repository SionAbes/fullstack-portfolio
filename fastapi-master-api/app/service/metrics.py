from typing import List

from app.domain import metric as domain
from app.domain.user_token import LoggedUser
from app.repository.database.metrics import MetricsRepo, metrics_repo
from app.service.authorization import authorize
from sqlalchemy.orm import Session


class CreateMetric:
    def __init__(
        self,
        db: Session,
        token: LoggedUser,
        create_metric: domain.CreateMetric,
        metric: domain.Metric = domain.Metric,
        metric_repo: MetricsRepo = metrics_repo,
    ):
        self.db = db
        self.token = token
        self.create_metric = create_metric
        self.metric = metric
        self.metric_repo = metric_repo

    def create(self) -> domain.Metric:
        self._authorize()
        return self._create()

    def _create(self) -> domain.Metric:
        return self.metric_repo.create(
            db=self.db,
            obj_in=self.create_metric,
        )

    def _authorize(self):
        self.options = self._build_options()
        authorize(
            self.token,
            self.metric,
            "create",
            self.db,
            self.options,
        )

    def _build_options(self) -> dict:
        return {
            "user_id": self.create_metric.user_id,
        }
