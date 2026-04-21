import json

from aenum import Enum


class UsageType(str, Enum):
    """
    The customer segment of the account.
    """

    """
    allowed enum values
    """
    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> "UsageType":
        """Create an instance of UsageType from a JSON string"""
        return UsageType(json.loads(json_str))
