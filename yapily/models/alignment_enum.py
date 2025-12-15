from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlignmentEnum(str, Enum):
    """
    allowed enum values
    """

    CONSENT = "CONSENT"
    CALENDAR = "CALENDAR"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
