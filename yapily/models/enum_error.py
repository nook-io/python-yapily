from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EnumError(str, Enum):
    """
    allowed enum values
    """

    MANDATORY = "MANDATORY"
    INVALID_FORMAT = "INVALID_FORMAT"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
