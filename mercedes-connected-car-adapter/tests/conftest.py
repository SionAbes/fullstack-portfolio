import pytest
from src.settings import Settings


def get_settings_override():
    return Settings(
        TOKEN="a1b2c3d4-a1b2-a1b2-a1b2-a1b2c3d4e5f6",
        CONNECTED_CAR_API_URL=(
            "https://api.mercedes-benz.com/experimental/connectedvehicle_tryout/v2"
        ),
    )


@pytest.fixture(scope="function")
def settings():
    return get_settings_override()
