from typing import Protocol


class Policy(Protocol):
    """Policy's public interface is designed around the convention of endpoint CRUD
    operations to keep policies and their consumers loosely coupled.
    See: https://gitlab.com/tacto/tacto/-/tree/master/docs/architecture#policy-methods"""

    def read(self) -> bool:
        return False

    def list(self) -> bool:
        return False

    def create(self) -> bool:
        return False

    def update(self) -> bool:
        return False

    def delete(self) -> bool:
        return False

    def _can_read(self) -> bool:
        return False

    def _can_write(self) -> bool:
        return False
