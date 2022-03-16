from typing import List

from app.api.manual_models.token import TokenModel


class LoggedUser:
    """This class acts as a wraper of the TokenModel to reduce the coupling with the low-level
    details of JWT token. It implements a slitghly more abstract API that is closer to `domain.User`
    and as a result, consumers don't need to know about `role`, `sub` org `org`."""

    def __init__(self, token: TokenModel):
        self.token = token

    @property
    def type(self) -> str:
        return self.token.type

    @property
    def expiration_time(self) -> int:
        return self.token.exp

    @property
    def issued_at(self) -> str:
        return self.token.iat

    @property
    def id(self) -> int:
        return self.token.sub

    @property
    def roles(self) -> List[str]:
        return self.token.roles

    def is_admin(self) -> bool:
        return "ADMIN" in self.token.roles
