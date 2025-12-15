from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PaymentContextTypeResponse(str, Enum):
    """
    allowed enum values
    """

    BILL = "BILL"
    GOODS = "GOODS"
    SERVICES = "SERVICES"
    OTHER = "OTHER"
    PERSON_TO_PERSON = "PERSON_TO_PERSON"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
