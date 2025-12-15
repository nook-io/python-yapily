from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AccountBalanceType(str, Enum):
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
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
