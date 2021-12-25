from datetime import datetime, timedelta

import pytz
from app.api.manual_models.token import TokenModel
from factory import Factory


class TokenModelFactory(Factory):
    class Meta:
        model = TokenModel

    sub = 1
    type = "access_token"
    exp = (datetime.now(pytz.utc) + timedelta(days=1)).timestamp()
    iat = str(datetime.now(pytz.utc))
    roles = ["ADMIN", "USER"]