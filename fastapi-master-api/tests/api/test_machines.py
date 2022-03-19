from datetime import datetime

from fastapi import status
from tests.factories.machine import MachineFactory


def test_fetch_machines_as_admin(
    app,
    client,
    mock_admin_user,
    auth_user,
):
    machine = MachineFactory(user=auth_user)

    url = app.url_path_for("fetch_machines")
    resp = client.get(url)
    machine_resp = resp.json()[0]

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 1
    assert machine_resp["user_id"] == machine.user_id
    assert machine_resp["oem_name"] == machine.oem_name
    assert machine_resp["model"] == machine.model
    assert machine_resp["make"] == machine.make
    assert machine_resp["equipment_id"] == machine.equipment_id
    assert machine_resp["serial_number"] == machine.serial_number
    assert machine_resp["pin"] == machine.pin


def test_fetch_machines_as_user(
    app,
    client,
    mock_standard_user,
    auth_user,
):
    MachineFactory.create_batch(2, user=auth_user)
    MachineFactory.create_batch(3)

    url = app.url_path_for("fetch_machines")
    resp = client.get(url)
    machine_resp = resp.json()[0]

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 2


def test_create_machine(
    app,
    client,
    mock_admin_user,
    auth_user,
):
    data = {
        "user_id": auth_user.id,
        "unit_installed_at": datetime.utcnow().isoformat(),
        "oem_name": "test_oem",
        "model": "test_model",
        "make": "test_make",
        "equipment_id": "test_equipment_id",
        "serial_number": "test_serial_number",
        "pin": "test_pin",
    }

    url = app.url_path_for("create_machine")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json()["user_id"] == data["user_id"]
    assert resp.json()["oem_name"] == data["oem_name"]
    assert resp.json()["model"] == data["model"]
    assert resp.json()["make"] == data["make"]
    assert resp.json()["equipment_id"] == data["equipment_id"]
    assert resp.json()["serial_number"] == data["serial_number"]
    assert resp.json()["pin"] == data["pin"]


def test_create_machine_not_authorized(
    app,
    client,
    mock_standard_user,
    auth_user,
):
    data = {
        "user_id": -1,
        "unit_installed_at": datetime.utcnow().isoformat(),
        "oem_name": "test_oem",
        "model": "test_model",
        "make": "test_make",
        "equipment_id": "test_equipment_id",
        "serial_number": "test_serial_number",
        "pin": "test_pin",
    }

    url = app.url_path_for("create_machine")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_403_FORBIDDEN
