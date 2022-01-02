from fastapi import status
from tests.factories.adapter import AdapterFactory


def test_create_adapter_no_body(
    app,
    client,
    mock_admin_user,
):
    url = app.url_path_for("create_adapter")
    resp = client.post(url)

    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_adapter_no_user(
    app,
    client,
):
    url = app.url_path_for("create_adapter")
    resp = client.post(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_adapter_standard_user(app, client, mock_standard_user):
    url = app.url_path_for("create_adapter")
    resp = client.post(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_adapter(app, client, mock_admin_user):
    data = {"adapter_name": "mercedes_connected_car", "cron_expression": "0 * * * *"}
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json().items() >= data.items()
    assert resp.json()["user_id"] == mock_admin_user.sub


def test_create_adapter_conflict(app, client, auth_user, mock_admin_user):
    data = {"adapter_name": "mercedes_connected_car", "cron_expression": "0 * * * *"}
    AdapterFactory(
        adapter_name=data["adapter_name"],
        cron_expression=data["cron_expression"],
        user=auth_user,
    )
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_409_CONFLICT
