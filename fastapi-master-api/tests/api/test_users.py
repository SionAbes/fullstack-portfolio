from tests.factories.user import UserFactory
from fastapi import status


def test_fetch_users(
    app,
    client,
    mock_admin_user,
):
    UserFactory.create_batch(2)
    url = app.url_path_for("fetch_users")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 3


def test_fetch_users_empty_db(
    app,
    client,
    mock_admin_user,
):
    url = app.url_path_for("fetch_users")
    resp = client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 1


def test_fetch_users_not_auth(
    app,
    client,
):
    UserFactory()
    url = app.url_path_for("fetch_users")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_fetch_users_auth_as_standard_user(
    app,
    client,
    mock_standard_user
):
    UserFactory()
    url = app.url_path_for("fetch_users")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED