from datetime import datetime

from app.repository.models.users import User
from factory import Faker, LazyFunction, RelatedFactory, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from tests import Session


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n)
    is_superuser = Faker("boolean")
    last_login_at = LazyFunction(lambda: datetime.now())
    created_at = LazyFunction(lambda: datetime.now())
    updated_at = LazyFunction(lambda: datetime.now())
    password = Faker("password")
    email = Faker("ascii_email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
