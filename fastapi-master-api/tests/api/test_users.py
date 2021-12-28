import pytest
from app.api.models.update_user import UpdateUser
from fastapi import status
from tests.factories.user import UserFactory


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


def test_fetch_users_auth_as_standard_user(app, client, mock_standard_user):
    UserFactory()
    url = app.url_path_for("fetch_users")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize(
    "data",
    [
        (
            UpdateUser(
                is_superuser=True,
            )
        ),
        (
            UpdateUser(
                is_superuser=True,
                last_name="_last_name",
            )
        ),
        (
            UpdateUser(
                is_superuser=True,
                first_name="_first_name",
            )
        ),
        (
            UpdateUser(
                is_superuser=True,
                email="_email",
            )
        ),
        (
            UpdateUser(
                last_name="_last_name",
            )
        ),
        (
            UpdateUser(
                last_name="_last_name",
                first_name="_first_name",
            )
        ),
        (
            UpdateUser(
                last_name="_last_name",
                first_name="_first_name",
                email="_email",
            )
        ),
        (
            UpdateUser(
                last_name="_last_name",
                email="_email",
            )
        ),
        (
            UpdateUser(
                first_name="_first_name",
            )
        ),
        (
            UpdateUser(
                first_name="_first_name",
                email="email",
            )
        ),
        (
            UpdateUser(
                first_name="_first_name",
                email="email",
                is_superuser=True,
            )
        ),
        (
            UpdateUser(
                last_name="_last_name",
                email="email",
                is_superuser=True,
            )
        ),
        (
            UpdateUser(
                first_name="_first_name",
                last_name="_last_name",
                email="email",
                is_superuser=True,
            )
        ),
    ],
)
def test_update_user_by_id(app, client, mock_admin_user, data):
    user = UserFactory(
        is_superuser=True,
        first_name="_first_name",
        last_name="_last_name",
        email="_email",
        password="_password",
    )
    url = app.url_path_for("update_user_by_id", id=user.id)
    resp = client.put(url, json=data.dict())
    user_data = user.__dict__ | data.dict(exclude_unset=True)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["is_superuser"] == user_data["is_superuser"]
    assert resp.json()["first_name"] == user_data["first_name"]
    assert resp.json()["last_name"] == user_data["last_name"]
    assert resp.json()["email"] == user_data["email"]
    assert resp.json()["id"] == user_data["id"]
