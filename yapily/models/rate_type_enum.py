from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RateTypeEnum(str, Enum):
    """
    allowed enum values
    """

    ACTUAL = "ACTUAL"
    AGREED = "AGREED"
    INDICATIVE = "INDICATIVE"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
