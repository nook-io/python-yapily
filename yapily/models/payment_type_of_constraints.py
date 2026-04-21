import json

from aenum import Enum


class PaymentTypeOfConstraints(str, Enum):
    """
    Payment type associated with constraints.
    """

    """
    allowed enum values
    """
    DOMESTIC_PAYMENT = "DOMESTIC_PAYMENT"
    DOMESTIC_INSTANT_PAYMENT = "DOMESTIC_INSTANT_PAYMENT"
    DOMESTIC_VARIABLE_RECURRING_PAYMENT = "DOMESTIC_VARIABLE_RECURRING_PAYMENT"
    DOMESTIC_SCHEDULED_PAYMENT = "DOMESTIC_SCHEDULED_PAYMENT"
    DOMESTIC_PERIODIC_PAYMENT = "DOMESTIC_PERIODIC_PAYMENT"
    INTERNATIONAL_PAYMENT = "INTERNATIONAL_PAYMENT"
    INTERNATIONAL_SCHEDULED_PAYMENT = "INTERNATIONAL_SCHEDULED_PAYMENT"
    INTERNATIONAL_PERIODIC_PAYMENT = "INTERNATIONAL_PERIODIC_PAYMENT"

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentTypeOfConstraints":
        """Create an instance of PaymentTypeOfConstraints from a JSON string"""
        return PaymentTypeOfConstraints(json.loads(json_str))
