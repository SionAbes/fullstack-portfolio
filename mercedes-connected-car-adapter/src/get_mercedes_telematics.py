import asyncio
from typing import Dict, List

import requests
from requests import Response
from src.models.distance import Distance
from src.models.doors import Doors
from src.models.fuel import Fuel
from src.models.location import Location
from src.models.tires import Tires
from src.models.vehicle import Vehicle
from src.settings import Settings, get_settings

TIMESERIES_METRICS = [
    {
        "endpoint_name": "doors",
        "model": Doors,
    },
    {
        "endpoint_name": "tires",
        "model": Tires,
    },
    {
        "endpoint_name": "odometer",
        "model": Distance,
    },
    {
        "endpoint_name": "fuel",
        "model": Fuel,
    },
    {
        "endpoint_name": "location",
        "model": Location,
    },
]


def get_vehicle_id_list(token: str, settings: Settings) -> List[Dict]:
    headers: dict = {"Authorization": f"Bearer {token}"}
    response: Response = requests.get(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles", headers=headers
    )
    return response.json()


def get_vehicle_details(vehicle_id: str, token: str, settings: Settings) -> Vehicle:
    headers: dict = {"Authorization": f"Bearer {token}"}
    response: Response = requests.get(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles/{vehicle_id}", headers=headers
    )
    vehicle_data = response.json()
    return Vehicle(
        make="mercedes_benz",
        model_year=vehicle_data["modelyear"],
        model=vehicle_data["salesdesignation"],
        license_plate=vehicle_data["licenseplate"],
        vin=vehicle_data["finorvin"],
    )


async def get_timeseries_information(
    metric: dict, vehicle_id: str, token: str, settings: Settings
):
    metrics: list = []
    endpoint_name: str = metric["endpoint_name"]
    headers: dict = {"Authorization": f"Bearer {token}"}
    response: Response = requests.get(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles/{vehicle_id}/{endpoint_name}",
        headers=headers,
    )
    response_data = response.json()
    metrics.append(metric["model"](**response_data))
    return metrics


async def main():
    settings = get_settings()
    token: str = settings.TOKEN

    vehicle_id_list = get_vehicle_id_list(token=token, settings=settings)
    vehicles = []
    for vehicle_id in vehicle_id_list:
        vehicles.append(
            get_vehicle_details(
                vehicle_id=vehicle_id["id"], token=token, settings=settings
            )
        )
        await asyncio.gather(
            *[
                get_timeseries_information(
                    metric=metric,
                    vehicle_id=vehicle_id["id"],
                    token=token,
                    settings=settings,
                )
                for metric in TIMESERIES_METRICS
            ]
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
