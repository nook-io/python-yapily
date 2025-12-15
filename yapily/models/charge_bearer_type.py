from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ChargeBearerType(str, Enum):
    """
    allowed enum values
    """

    DEBT = "DEBT"
    CRED = "CRED"
    SHAR = "SHAR"
    SLEV = "SLEV"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
