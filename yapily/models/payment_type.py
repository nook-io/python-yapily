import json

from aenum import Enum


class PaymentType(str, Enum):
    """
    __Mandatory__. Used to specify which of the [payment types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#payment-types) to execute.<br><br>See [European Payments](https://docs.yapily.com/pages/knowledge/open-banking/european_payments/) to verify whether the `type` should be `DOMESTIC` or `INTERNATIONAL`.
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
    def from_json(cls, json_str: str) -> "PaymentType":
        """Create an instance of PaymentType from a JSON string"""
        return PaymentType(json.loads(json_str))
