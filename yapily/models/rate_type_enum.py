import json

from aenum import Enum


class RateTypeEnum(str, Enum):
    """
    __Mandatory__. The type used to complete the currency exchange.
    """

    """
    allowed enum values
    """
    ACTUAL = "ACTUAL"
    AGREED = "AGREED"
    INDICATIVE = "INDICATIVE"

    @classmethod
    def from_json(cls, json_str: str) -> "RateTypeEnum":
        """Create an instance of RateTypeEnum from a JSON string"""
        return RateTypeEnum(json.loads(json_str))
