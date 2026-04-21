import json

from aenum import Enum


class EnumError(str, Enum):
    """
    EnumError
    """

    """
    allowed enum values
    """
    MANDATORY = "MANDATORY"
    INVALID_FORMAT = "INVALID_FORMAT"

    @classmethod
    def from_json(cls, json_str: str) -> "EnumError":
        """Create an instance of EnumError from a JSON string"""
        return EnumError(json.loads(json_str))
