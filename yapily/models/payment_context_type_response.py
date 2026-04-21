import json

from aenum import Enum


class PaymentContextTypeResponse(str, Enum):
    """
    The payment context code.
    """

    """
    allowed enum values
    """
    BILL = "BILL"
    GOODS = "GOODS"
    SERVICES = "SERVICES"
    OTHER = "OTHER"
    PERSON_TO_PERSON = "PERSON_TO_PERSON"

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentContextTypeResponse":
        """Create an instance of PaymentContextTypeResponse from a JSON string"""
        return PaymentContextTypeResponse(json.loads(json_str))
