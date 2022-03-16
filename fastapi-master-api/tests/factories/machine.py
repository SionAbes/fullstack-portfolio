from datetime import datetime

from app.repository.models.machines import Machine
from factory import Faker, LazyFunction, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from faker_vehicle import VehicleProvider
from tests import Session
from tests.factories.user import UserFactory

Faker.add_provider(VehicleProvider)


class MachineFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Machine
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    user = SubFactory(UserFactory)

    created_at = LazyFunction(lambda: datetime.now())
    updated_at = LazyFunction(lambda: datetime.now())
    unit_installed_at = LazyFunction(lambda: datetime.now())

    oem_name = Faker("company")
    model = Faker("vehicle_model")
    make = Faker("vehicle_make")
    equipment_id = Faker("license_plate")
    serial_number = Faker("ean")
    pin = Faker("ean8")
