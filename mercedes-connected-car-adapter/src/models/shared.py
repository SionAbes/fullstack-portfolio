from enum import Enum


class RetrievalStatus(Enum):
    VALID = "VALID"
    INITIALIZED = "INITIALIZED"
    INVALID = "INVALID"
    NOT_SUPPORTED = "NOT_SUPPORTED"
