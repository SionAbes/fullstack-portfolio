from datetime import datetime, timedelta

import jwt
from app.domain.auth import create_token
from freezegun import freeze_time


@freeze_time(datetime(2015, 5, 1, 15, 20, 30))
def test_create_token(freezer, mock_admin_user):
    token = create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=10),
        sub=mock_admin_user.sub,
        roles=mock_admin_user.roles,
    )
    decoded_token = jwt.decode(token, "jwt_secret", algorithms=["HS256"])
    assert decoded_token["roles"] == ["ADMIN", "USER"]
    assert int(decoded_token["sub"]) == mock_admin_user.sub
    assert decoded_token["type"] == mock_admin_user.type
    assert datetime.fromtimestamp(decoded_token["iat"]).year == datetime.now().year
    assert datetime.fromtimestamp(decoded_token["iat"]).month == datetime.now().month
    assert datetime.fromtimestamp(decoded_token["iat"]).day == datetime.now().day
    assert datetime.fromtimestamp(decoded_token["iat"]).hour == datetime.now().hour
    assert datetime.fromtimestamp(decoded_token["iat"]).minute == datetime.now().minute
    assert datetime.fromtimestamp(decoded_token["iat"]).second == datetime.now().second
    assert datetime.fromtimestamp(decoded_token["exp"]).year == datetime.now().year
    assert datetime.fromtimestamp(decoded_token["exp"]).month == datetime.now().month
    assert datetime.fromtimestamp(decoded_token["exp"]).day == datetime.now().day
    assert datetime.fromtimestamp(decoded_token["exp"]).hour == datetime.now().hour
    assert (
        datetime.fromtimestamp(decoded_token["exp"]).minute
        == (datetime.now() + timedelta(minutes=10)).minute
    )
    assert datetime.fromtimestamp(decoded_token["exp"]).second == datetime.now().second
