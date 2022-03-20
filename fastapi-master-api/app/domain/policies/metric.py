from app.domain.user_token import LoggedUser
from app.service.exceptions import EntityNotFoundError
from sqlalchemy.orm import Session

from .base import Policy


class MetricPolicy(Policy):
    def __init__(
        self,
        subject: LoggedUser,
        metric_id: int,
        db: Session,
        options: dict = {},
    ):
        self.db = db
        self.subject = subject
        self.metric_id = metric_id
        self.options = options

    def create(self) -> bool:
        if not self.subject.is_admin():
            return self.options["user_id"] == self.subject.id
        return True
