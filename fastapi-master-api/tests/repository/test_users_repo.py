from app.repository.database.users import users_repo
from tests.factories.user import UserFactory
import pytest

def test_get_by_email(session, freezer):
    user = UserFactory()
    user_db = users_repo.get_by_email(
        db=session,
        email=user.email
    )
    assert user_db.first_name == user.first_name
    assert user_db.last_name == user.last_name
    assert user_db.id == user.id
    assert user_db.created_at == user.created_at
    assert user_db.is_superuser == user.is_superuser
    assert user_db.email == user.email
    assert user_db.last_login_at == user.last_login_at


def test_get_by_email_not_exists(session, freezer):
    user = UserFactory()
    user_db = users_repo.get_by_email(
        db=session,
        email="_email"
    )
    assert user_db is None


def test_get_by_email_no_session(freezer):
    user = UserFactory()
    with pytest.raises(AttributeError):
        users_repo.get_by_email(
            db=None,
            email=user.email
        )