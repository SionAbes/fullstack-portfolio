from unittest.mock import Mock, patch

import requests
from src.get_mercedes_telematics import get_vehicle_details, get_vehicle_id_list
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
