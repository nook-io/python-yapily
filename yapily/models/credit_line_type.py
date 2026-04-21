import json

from aenum import Enum


class CreditLineType(str, Enum):
    """
    __Mandatory__. The type of credit that has been provided.
    """

    """
    allowed enum values
    """
    AVAILABLE = "AVAILABLE"
    CREDIT = "CREDIT"
    EMERGENCY = "EMERGENCY"
    PRE_AGREED = "PRE_AGREED"
    TEMPORARY = "TEMPORARY"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> "CreditLineType":
        """Create an instance of CreditLineType from a JSON string"""
        return CreditLineType(json.loads(json_str))
