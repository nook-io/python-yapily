import json

from aenum import Enum


class PaymentContextType(str, Enum):
    """
    __Optional__. The payment context code. This defaults to `OTHER` if not specified.
    """

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
    def from_json(cls, json_str: str) -> "PaymentContextType":
        """Create an instance of PaymentContextType from a JSON string"""
        return PaymentContextType(json.loads(json_str))
