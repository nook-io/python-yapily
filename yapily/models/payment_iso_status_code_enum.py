import json

from aenum import Enum


class PaymentIsoStatusCodeEnum(str, Enum):
    """
    The ISO 20022 `PaymentStatusCode`.
    """

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
    def from_json(cls, json_str: str) -> "PaymentIsoStatusCodeEnum":
        """Create an instance of PaymentIsoStatusCodeEnum from a JSON string"""
        return PaymentIsoStatusCodeEnum(json.loads(json_str))
