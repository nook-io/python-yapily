from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PaymentContextType(str, Enum):
    """
    allowed enum values
    """

    BILL = "BILL"
    GOODS = "GOODS"
    SERVICES = "SERVICES"
    OTHER = "OTHER"
    PERSON_TO_PERSON = "PERSON_TO_PERSON"
    BILL_IN_ADVANCE = "BILL_IN_ADVANCE"
    BILL_IN_ARREARS = "BILL_IN_ARREARS"
    ECOMMERCE_MERCHANT = "ECOMMERCE_MERCHANT"
    FACE_TO_FACE_POS = "FACE_TO_FACE_POS"
    TRANSFER_TO_SELF = "TRANSFER_TO_SELF"
    TRANSFER_TO_THIRD_PARTY = "TRANSFER_TO_THIRD_PARTY"
    PISP_PAYEE = "PISP_PAYEE"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
