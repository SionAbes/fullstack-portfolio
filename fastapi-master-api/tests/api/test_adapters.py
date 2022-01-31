from app.security import verify_string_hash
from fastapi import status


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


def test_create_adapter_volvo_caretrack(
    app,
    client,
    mock_admin_user,
):
    data = {
        "adapter_name": "volvo_caretrack",
        "data_url": "_data_url",
        "cron_expression": "1 * * * *",
        "username": "_username",
        "password": "_password",
    }
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["adapter_name"] == data["adapter_name"]
    assert resp.json()["data_url"] == data["data_url"]
    assert resp.json()["cron_expression"] == data["cron_expression"]
    assert resp.json()["username"] == data["username"]
    assert verify_string_hash(data["password"], resp.json()["password"])
    assert resp.json()["user_id"] == mock_admin_user.sub


def test_create_adapter_wacker_neuson_kramer(
    app,
    client,
    mock_admin_user,
):
    data = {
        "adapter_name": "wacker_neuson_kramer",
        "data_url": "_data_url",
        "cron_expression": "1 * * * *",
        "token_url": "_token_url",
        "username": "_username",
        "password": "_password",
        "client_id": "_client_id",
        "client_secret": "_client_secret",
    }
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["adapter_name"] == data["adapter_name"]
    assert resp.json()["data_url"] == data["data_url"]
    assert resp.json()["cron_expression"] == data["cron_expression"]
    assert resp.json()["username"] == data["username"]
    assert verify_string_hash(data["password"], resp.json()["password"])
    assert verify_string_hash(data["client_id"], resp.json()["client_id"])
    assert verify_string_hash(data["client_secret"], resp.json()["client_secret"])
    assert resp.json()["user_id"] == mock_admin_user.sub


def test_create_adapter_lidat_liebherr(
    app,
    client,
    mock_admin_user,
):
    data = {
        "adapter_name": "liebherr_lidat",
        "data_url": "_data_url",
        "cron_expression": "1 * * * *",
        "username": "_username",
        "password": "_password",
    }
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["adapter_name"] == data["adapter_name"]
    assert resp.json()["data_url"] == data["data_url"]
    assert resp.json()["cron_expression"] == data["cron_expression"]
    assert resp.json()["username"] == data["username"]
    assert verify_string_hash(data["password"], resp.json()["password"])
    assert resp.json()["user_id"] == mock_admin_user.sub


def test_create_adapter_takeuchi_tfm(
    app,
    client,
    mock_admin_user,
):
    data = {
        "adapter_name": "takeuchi_tfm",
        "data_url": "_data_url",
        "cron_expression": "1 * * * *",
        "token_url": "_token_url",
        "client_id": "_client_id",
        "client_secret": "_client_secret",
    }
    url = app.url_path_for("create_adapter")
    resp = client.post(url, json=data)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["adapter_name"] == data["adapter_name"]
    assert resp.json()["data_url"] == data["data_url"]
    assert resp.json()["cron_expression"] == data["cron_expression"]
    assert verify_string_hash(data["client_id"], resp.json()["client_id"])
    assert verify_string_hash(data["client_secret"], resp.json()["client_secret"])
    assert resp.json()["user_id"] == mock_admin_user.sub
