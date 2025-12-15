from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PaymentStatus(str, Enum):
    """
    allowed enum values
    """

    PENDING = "PENDING"
    FAILED = "FAILED"
    DECLINED = "DECLINED"
    COMPLETED = "COMPLETED"
    COMPLETED_SETTLEMENT_IN_PROCESS = "COMPLETED_SETTLEMENT_IN_PROCESS"
    EXPIRED = "EXPIRED"
    UNKNOWN = "UNKNOWN"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
