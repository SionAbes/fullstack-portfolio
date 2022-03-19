from inspect import isclass
from typing import Optional

from app.domain.policies import POLICIES_REGISTRY, Policy
from app.domain.user_token import LoggedUser
from sqlalchemy.orm import Session


class NotAuthorizedError(Exception):
    def __init__(self):
        self.type = "NOT_AUTHORIZED"


def authorize(
    subject: LoggedUser,
    data_object,
    action: str,
    db: Optional[Session] = None,
    options: dict = {},
) -> None:
    if not data_object:
        raise NotAuthorizedError

    policy_class = _resolve_policy(data_object)

    if type(data_object) == tuple:
        data_object = data_object[0]

    policy = policy_class(subject, data_object, db=db, options=options)
    method = getattr(policy_class, action)

    if not method(policy):
        raise NotAuthorizedError()


class ResolutionError(Exception):
    pass


class RegistryClassResolver:
    def resolve(self, data_object) -> Policy:
        return POLICIES_REGISTRY[data_object.__name__]


class RegistryResolver:
    def resolve(self, data_object) -> Policy:
        object_class = type(data_object).__name__
        policy = POLICIES_REGISTRY.get(object_class)
        if not policy:
            raise ResolutionError
        return policy


class IdResolver:
    def resolve(self, data_object) -> Policy:
        _, object_class = data_object
        policy = POLICIES_REGISTRY.get(object_class)
        if not policy:
            raise ResolutionError
        return policy


def _resolve_policy(data_object):
    """You need to map domain entity and its policy in the `POLICIES_REGISTRY`"""

    if isclass(data_object):
        resolution_strategy = RegistryClassResolver
    else:
        resolution_strategy = RegistryResolver

    try:
        policy = resolution_strategy().resolve(data_object)
    except ResolutionError:
        policy = IdResolver().resolve(data_object)

    return policy
