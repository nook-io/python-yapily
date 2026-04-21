import json

from aenum import Enum


class PriorityCodeEnum(str, Enum):
    """
    PriorityCodeEnum
    """

    """
    allowed enum values
    """
    NORMAL = "NORMAL"
    URGENT = "URGENT"

    @classmethod
    def from_json(cls, json_str: str) -> "PriorityCodeEnum":
        """Create an instance of PriorityCodeEnum from a JSON string"""
        return PriorityCodeEnum(json.loads(json_str))
