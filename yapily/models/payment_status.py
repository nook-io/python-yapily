import json

from aenum import Enum


class PaymentStatus(str, Enum):
    """
    The status of the Payment. <br><br>For more information, see [Payment Status](/guides/payments/payment-status/)
    """

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
    def from_json(cls, json_str: str) -> "PaymentStatus":
        """Create an instance of PaymentStatus from a JSON string"""
        return PaymentStatus(json.loads(json_str))
