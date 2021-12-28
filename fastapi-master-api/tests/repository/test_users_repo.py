import pytest
from app.domain.models.user import CreateUser
from app.repository.database.users import users_repo
from tests.factories.user import UserFactory


def test_get(session, freezer):
    user = UserFactory()
    user_db = users_repo.get(db=session, id=user.id)
    assert user_db.first_name == user.first_name
    assert user_db.last_name == user.last_name
    assert user_db.id == user.id
    assert user_db.created_at == user.created_at
    assert user_db.is_superuser == user.is_superuser
    assert user_db.email == user.email
    assert user_db.last_login_at == user.last_login_at


def test_get_no_user(session):
    user_db = users_repo.get(db=session, id=-1)
    assert user_db == None


def test_list(session, freezer):
    UserFactory.create_batch(2)
    user_db = users_repo.list(
        db=session,
    )
    assert len(user_db) == 2


def test_update(session):
    user_update = CreateUser(
        is_superuser=True,
        first_name="_first_name",
        last_name="_last_name",
        email="_email",
        password="_password",
    )
    user = UserFactory()
    user_db = users_repo.update(
        db=session,
        id=user.id,
        obj_in=user_update,
    )
    assert user_db.first_name == user.first_name
    assert user_db.last_name == user.last_name
    assert user_db.is_superuser == user.is_superuser
    assert user_db.email == user.email


def test_get_by_email(session, freezer):
    user = UserFactory()
    user_db = users_repo.get_by_email(db=session, email=user.email)
    assert user_db.first_name == user.first_name
    assert user_db.last_name == user.last_name
    assert user_db.id == user.id
    assert user_db.created_at == user.created_at
    assert user_db.is_superuser == user.is_superuser
    assert user_db.email == user.email
    assert user_db.last_login_at == user.last_login_at


def test_get_by_email_not_exists(session, freezer):
    UserFactory()
    user_db = users_repo.get_by_email(db=session, email="_email")
    assert user_db is None


def test_get_by_email_no_session(freezer):
    user = UserFactory()
    with pytest.raises(AttributeError):
        users_repo.get_by_email(db=None, email=user.email)


def test_create(session):
    user = CreateUser(
        is_superuser=True,
        first_name="_first_name",
        last_name="_last_name",
        email="_email",
        password="_password",
    )
    user_db = users_repo.create(db=session, obj_in=user)
    assert user_db.first_name == user.first_name
    assert user_db.last_name == user.last_name
    assert user_db.is_superuser == user.is_superuser
    assert user_db.email == user.email


def test_create_no_user(session):
    with pytest.raises(AttributeError):
        users_repo.create(db=session, obj_in=None)
