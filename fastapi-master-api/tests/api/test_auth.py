from fastapi import status


def test_login(
    app,
    client,
    mock_admin_user,
):
    data = {
        "grant_type": None,
        "username": "test_email",
        "password": "test_password",
        "scope": None,
        "client_id": None,
        "client_secret": None,
    }
    url = app.url_path_for("login")
    resp = client.post(url, data=data)
    assert resp.status_code == status.HTTP_200_OK


def test_login_bad_password(
    app,
    client,
    mock_admin_user,
):
    data = {
        "grant_type": None,
        "username": "test_email",
        "password": "bad_password",
        "scope": None,
        "client_id": None,
        "client_secret": None,
    }
    url = app.url_path_for("login")
    resp = client.post(url, data=data)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST


def test_login_user_not_exist(
    app,
    client,
    mock_admin_user,
):
    data = {
        "grant_type": None,
        "username": "bad_email",
        "password": "bad_password",
        "scope": None,
        "client_id": None,
        "client_secret": None,
    }
    url = app.url_path_for("login")
    resp = client.post(url, data=data)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


def test_refresh(
    app,
    client,
    refresh_token,
):
    url = app.url_path_for("refresh")
    resp = client.post(url)
    assert resp.status_code == status.HTTP_200_OK


def test_refresh_incorrect_type(
    app,
    client,
    mock_admin_user,
):
    url = app.url_path_for("refresh")
    resp = client.post(url)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
