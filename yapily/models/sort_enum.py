from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SortEnum(str, Enum):
    """
    allowed enum values
    """

    DATE = "date"
    MINUS_DATE = "-date"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
