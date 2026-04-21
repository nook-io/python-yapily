import json

from aenum import Enum


class SortEnum(str, Enum):
    """
    The attribute on which resources / records returned should be sorted. Valid options for the sort parameter.
    """

    """
    allowed enum values
    """
    DATE = "date"
    MINUS_DATE = "-date"

    @classmethod
    def from_json(cls, json_str: str) -> "SortEnum":
        """Create an instance of SortEnum from a JSON string"""
        return SortEnum(json.loads(json_str))
