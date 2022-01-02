from unittest.mock import patch

import pytest
import requests
from src.get_mercedes_telematics import (
    TIMESERIES_METRICS,
    get_timeseries_information,
    get_vehicle_details,
    get_vehicle_id_list,
)
from src.models.vehicle import Vehicle


@patch.object(requests, "get")
def test_get_vehicle_id_list(mock_request_post, settings):
    token = "_token"
    data = [
        {
            "id": "1234567890ABCD1234",
            "licenseplate": "HD-AB-123",
            "finorvin": "WDD***********123",
        }
    ]

    def res():
        r = requests.Response()
        r.status_code = 200

        def json_func():
            return data

        r.json = json_func
        return r

    mock_request_post.return_value = res()
    assert data == get_vehicle_id_list(token=token, settings=settings)
    mock_request_post.assert_called_with(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles",
        headers={"Authorization": f"Bearer {token}"},
    )


@patch.object(requests, "get")
def test_get_vehicle_details(mock_request_post, settings):
    token = "_token"
    vehicle_id = "1234567890ABCD1234"
    data = {
        "id": "1234567890ABCD1234",
        "licenseplate": "HD-AB-123",
        "salesdesignation": "E 400 4MATIC Limousine",
        "finorvin": "WDD***********123",
        "nickname": "mmueller",
        "modelyear": "2017",
        "colorname": "iridiumsilber metallic",
        "fueltype": "Benzin",
        "powerhp": "333",
        "powerkw": "245",
        "numberofdoors": "5",
        "numberofseats": "5",
    }

    def res():
        r = requests.Response()
        r.status_code = 200

        def json_func():
            return data

        r.json = json_func
        return r

    vehicle_data = Vehicle(
        make="mercedes_benz",
        model_year=data["modelyear"],
        model=data["salesdesignation"],
        license_plate=data["licenseplate"],
        vin=data["finorvin"],
    )

    mock_request_post.return_value = res()
    assert vehicle_data == get_vehicle_details(
        vehicle_id=vehicle_id, token=token, settings=settings
    )
    mock_request_post.assert_called_with(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles/{vehicle_id}",
        headers={"Authorization": f"Bearer {token}"},
    )


@pytest.mark.asyncio
@patch.object(requests, "get")
async def test_get_timeseries_information(mock_request_post, settings):
    token = "_token"
    vehicle_id = "1234567890ABCD1234"
    data = {
        "doorstatusfrontleft": {
            "value": "OPEN",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusfrontleft": {
            "value": "UNLOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorstatusfrontright": {
            "value": "CLOSED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusfrontright": {
            "value": "LOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorstatusrearleft": {
            "value": "CLOSED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusrearleft": {
            "value": "LOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorstatusrearright": {
            "value": "OPEN",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusrearright": {
            "value": "LOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusdecklid": {
            "value": "UNLOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusgas": {
            "value": "UNLOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
        "doorlockstatusvehicle": {
            "value": "UNLOCKED",
            "retrievalstatus": "VALID",
            "timestamp": 1641120470,
        },
    }

    def res():
        r = requests.Response()
        r.status_code = 200

        def json_func():
            return data

        r.json = json_func
        return r

    mock_request_post.return_value = res()
    assert [TIMESERIES_METRICS[0]["model"](**data)] == await get_timeseries_information(
        metric=TIMESERIES_METRICS[0],
        vehicle_id=vehicle_id,
        token=token,
        settings=settings,
    )
    mock_request_post.assert_called_with(
        f"{settings.CONNECTED_CAR_API_URL}/vehicles/{vehicle_id}/{TIMESERIES_METRICS[0]['endpoint_name']}",
        headers={"Authorization": f"Bearer {token}"},
    )
