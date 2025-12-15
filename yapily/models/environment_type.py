from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EnvironmentType(str, Enum):
    """
    allowed enum values
    """

    SANDBOX = "SANDBOX"
    MOCK = "MOCK"
    LIVE = "LIVE"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
