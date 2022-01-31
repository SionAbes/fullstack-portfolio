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
