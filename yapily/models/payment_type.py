# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentType from a JSON string"""
        return cls(json.loads(json_str))
