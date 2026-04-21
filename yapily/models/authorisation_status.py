import json

from aenum import Enum


class AuthorisationStatus(str, Enum):
    """
    Current status of the embedded authorisation request in code form.
    """

    """
    allowed enum values
    """
    AWAITING_AUTHORIZATION = "AWAITING_AUTHORIZATION"
    AWAITING_FURTHER_AUTHORIZATION = "AWAITING_FURTHER_AUTHORIZATION"
    AWAITING_RE_AUTHORIZATION = "AWAITING_RE_AUTHORIZATION"
    AUTHORIZED = "AUTHORIZED"
    CONSUMED = "CONSUMED"
    REJECTED = "REJECTED"
    REVOKED = "REVOKED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    UNKNOWN = "UNKNOWN"
    INVALID = "INVALID"
    AWAITING_DECOUPLED_PRE_AUTHORIZATION = "AWAITING_DECOUPLED_PRE_AUTHORIZATION"
    AWAITING_PRE_AUTHORIZATION = "AWAITING_PRE_AUTHORIZATION"
    PRE_AUTHORIZED = "PRE_AUTHORIZED"
    AWAITING_DECOUPLED_AUTHORIZATION = "AWAITING_DECOUPLED_AUTHORIZATION"
    AWAITING_SCA_METHOD = "AWAITING_SCA_METHOD"
    AWAITING_SCA_CODE = "AWAITING_SCA_CODE"

    @classmethod
    def from_json(cls, json_str: str) -> "AuthorisationStatus":
        """Create an instance of AuthorisationStatus from a JSON string"""
        return AuthorisationStatus(json.loads(json_str))
