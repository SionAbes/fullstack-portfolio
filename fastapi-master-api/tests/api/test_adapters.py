from app.dependancies import encrypt_string
from fastapi import status
from tests.factories.adapter import BearerTokenAdapterFactory


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


def test_create_adapter_bearer_token(app, client, mock_admin_user, settings):
    token = encrypt_string(
        string_to_encrypt="abcdefghijklmnopqrstuvwxyz", secret=settings.HASH_SECRET
    )
    data = {
        "adapter_name": "mercedes_connected_car",
        "cron_expression": "0 * * * *",
        "authorization_type": "bearer_token",
        "bearer_token": token,
    }
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["cron_expression"] >= data["cron_expression"]
    assert resp.json()["user_id"] == mock_admin_user.sub
    assert resp.json()["adapter_name"] >= data["adapter_name"]


def test_create_adapter_bearer_token_not_encrypted(
    app, client, mock_admin_user, settings
):
    data = {
        "adapter_name": "mercedes_connected_car",
        "cron_expression": "0 * * * *",
        "authorization_type": "bearer_token",
        "bearer_token": "abcdefghijklmnopqrstuvwxyz",
    }

    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_403_FORBIDDEN


def test_create_adapter_conflict(app, client, auth_user, mock_admin_user, settings):
    token = encrypt_string(
        string_to_encrypt="abcdefghijklmnopqrstuvwxyz", secret=settings.HASH_SECRET
    )
    data = {
        "adapter_name": "mercedes_connected_car",
        "cron_expression": "0 * * * *",
        "authorization_type": "bearer_token",
        "bearer_token": token,
    }
    BearerTokenAdapterFactory(
        adapter_name=data["adapter_name"],
        cron_expression=data["cron_expression"],
        user=auth_user,
    )
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_409_CONFLICT


def test_fetch_adapters(app, client, mock_admin_user, settings):
    token = encrypt_string(
        string_to_encrypt="abcdefghijklmnopqrstuvwxyz", secret=settings.HASH_SECRET
    )
    BearerTokenAdapterFactory.create_batch(2, bearer_token=token)
    url = app.url_path_for("fetch_adapters")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 2


def test_fetch_adapters_token_not_encrypted(
    app,
    client,
    mock_admin_user,
):
    BearerTokenAdapterFactory.create_batch(2, bearer_token="abcdefg")
    url = app.url_path_for("fetch_adapters")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_403_FORBIDDEN


def test_fetch_adapters_empty_db(
    app,
    client,
    mock_admin_user,
):
    url = app.url_path_for("fetch_adapters")
    resp = client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 0


def test_fetch_adapters_not_auth(
    app,
    client,
):
    BearerTokenAdapterFactory()
    url = app.url_path_for("fetch_adapters")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_fetch_adapters_auth_as_standard_user(app, client, mock_standard_user):
    BearerTokenAdapterFactory()
    url = app.url_path_for("fetch_users")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
