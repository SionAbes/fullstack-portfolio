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
