from datetime import datetime

from app.repository.models.adapters import Adapter
from factory import LazyFunction, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from tests import Session
from tests.factories.user import UserFactory


class AdapterFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Adapter
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n)
    created_at = LazyFunction(lambda: datetime.now())
    updated_at = LazyFunction(lambda: datetime.now())
    user = SubFactory(UserFactory)
    cron_expression = "0 * * * *"
    adapter_name = "mercedes_connected_car"
