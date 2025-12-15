from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WebhookStatusType(str, Enum):
    """
    allowed enum values
    """

    ACTIVE = "active"
    PAUSED = "paused"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
