import passlib
import pytest
from app.security import verify_string_hash


def test_verify_password():
    password = "test"
    hashed_password = "$2b$12$Dhp7oFAnpFeyLmA/tLAzhefy/ipC641qZg.3RNW0VvYmbqiQmHMLG"
    assert (
        verify_string_hash(unhashed_string=password, hashed_password=hashed_password)
        is True
    )


def test_verify_password_false():
    password = "test"
    hashed_password = "_hashed_password_false"
    with pytest.raises(passlib.exc.UnknownHashError):
        verify_string_hash(unhashed_string=password, hashed_password=hashed_password)
