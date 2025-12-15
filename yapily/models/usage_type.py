from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UsageType(str, Enum):
    """
    allowed enum values
    """

    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
