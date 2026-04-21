import json

from aenum import Enum


class PaymentTypeResponse(str, Enum):
    """
    Specifies which of the [payment types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#payment-types) to execute.<br>
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
    def from_json(cls, json_str: str) -> "PaymentTypeResponse":
        """Create an instance of PaymentTypeResponse from a JSON string"""
        return PaymentTypeResponse(json.loads(json_str))
