import json

from aenum import Enum


class TransactionStatusEnum(str, Enum):
    """
    TransactionStatusEnum
    """

    """
    allowed enum values
    """
    BOOKED = "BOOKED"
    PENDING = "PENDING"

    @classmethod
    def from_json(cls, json_str: str) -> "TransactionStatusEnum":
        """Create an instance of TransactionStatusEnum from a JSON string"""
        return TransactionStatusEnum(json.loads(json_str))
