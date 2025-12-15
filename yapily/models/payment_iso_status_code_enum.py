from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PaymentIsoStatusCodeEnum(str, Enum):
    """
    allowed enum values
    """

    ACCC = "ACCC"
    ACCP = "ACCP"
    ACSC = "ACSC"
    ACSP = "ACSP"
    ACTC = "ACTC"
    ACWC = "ACWC"
    ACWP = "ACWP"
    RCVD = "RCVD"
    PDNG = "PDNG"
    RJCT = "RJCT"
    CANC = "CANC"
    ACFC = "ACFC"
    PATC = "PATC"
    PART = "PART"
    ACCO = "ACCO"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
