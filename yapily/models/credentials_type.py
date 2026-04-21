import json

from aenum import Enum


class CredentialsType(str, Enum):
    """
    The type of credentials required to register the `Institution`
    """

    """
    allowed enum values
    """
    OAUTH1 = "OAUTH1"
    OAUTH2 = "OAUTH2"
    OAUTH2_NOSECRET = "OAUTH2_NOSECRET"
    OAUTH2_SIGNATURE = "OAUTH2_SIGNATURE"
    OPEN_BANKING_UK_MANUAL = "OPEN_BANKING_UK_MANUAL"
    OPEN_BANKING_UK_AUTO = "OPEN_BANKING_UK_AUTO"
    OPEN_BANKING_IBM = "OPEN_BANKING_IBM"
    OPEN_BANKING_AUTO = "OPEN_BANKING_AUTO"
    OPEN_BANKING_AUTO_EMAIL = "OPEN_BANKING_AUTO_EMAIL"
    OPEN_BANKING_MANUAL = "OPEN_BANKING_MANUAL"
    OPEN_BANKING_WITH_TPP_ID_AND_SECRET = "OPEN_BANKING_WITH_TPP_ID_AND_SECRET"
    API_KEY = "API_KEY"
    OPEN_BANKING_NO_KEY = "OPEN_BANKING_NO_KEY"
    OPEN_BANKING_NO_TRANSPORT = "OPEN_BANKING_NO_TRANSPORT"
    TOKEN_IO = "TOKEN_IO"

    @classmethod
    def from_json(cls, json_str: str) -> "CredentialsType":
        """Create an instance of CredentialsType from a JSON string"""
        return CredentialsType(json.loads(json_str))
