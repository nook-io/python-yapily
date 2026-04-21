import json

from aenum import Enum


class AccountBalanceType(str, Enum):
    """
    Specifies the type of the stated account balance.
    """

    """
    allowed enum values
    """
    CLOSING_AVAILABLE = "CLOSING_AVAILABLE"
    CLOSING_BOOKED = "CLOSING_BOOKED"
    CLOSING_CLEARED = "CLOSING_CLEARED"
    EXPECTED = "EXPECTED"
    FORWARD_AVAILABLE = "FORWARD_AVAILABLE"
    INFORMATION = "INFORMATION"
    INTERIM_AVAILABLE = "INTERIM_AVAILABLE"
    INTERIM_BOOKED = "INTERIM_BOOKED"
    INTERIM_CLEARED = "INTERIM_CLEARED"
    OPENING_AVAILABLE = "OPENING_AVAILABLE"
    OPENING_BOOKED = "OPENING_BOOKED"
    OPENING_CLEARED = "OPENING_CLEARED"
    PREVIOUSLY_CLOSED_BOOKED = "PREVIOUSLY_CLOSED_BOOKED"
    AUTHORISED = "AUTHORISED"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> "AccountBalanceType":
        """Create an instance of AccountBalanceType from a JSON string"""
        return AccountBalanceType(json.loads(json_str))
