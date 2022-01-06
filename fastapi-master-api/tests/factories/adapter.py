from datetime import datetime

from app.repository.models.adapters import AuthorizationBearerToken
from factory import Faker, LazyFunction, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from tests import Session
from tests.factories.user import UserFactory


class BearerTokenAdapterFactory(SQLAlchemyModelFactory):
    class Meta:
        model = AuthorizationBearerToken
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n)
    created_at = LazyFunction(lambda: datetime.now())
    updated_at = LazyFunction(lambda: datetime.now())
    user = SubFactory(UserFactory)
    cron_expression = "0 * * * *"
    adapter_name = "mercedes_connected_car"
    authorization_type = "bearer_token"
    auth_type_id = Sequence(lambda n: n)
    bearer_token = Faker("pystr")
