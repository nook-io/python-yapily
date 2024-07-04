# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import re  # noqa: F401

from aenum import Enum


class PaymentTypeResponse(str, Enum):
    """
    Specifies which of the [payment types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#payment-types) to execute.<br>
    """

    """
    allowed enum values
    """
    DOMESTIC_PAYMENT = 'DOMESTIC_PAYMENT'
    DOMESTIC_INSTANT_PAYMENT = 'DOMESTIC_INSTANT_PAYMENT'
    DOMESTIC_VARIABLE_RECURRING_PAYMENT = 'DOMESTIC_VARIABLE_RECURRING_PAYMENT'
    DOMESTIC_SCHEDULED_PAYMENT = 'DOMESTIC_SCHEDULED_PAYMENT'
    DOMESTIC_PERIODIC_PAYMENT = 'DOMESTIC_PERIODIC_PAYMENT'
    INTERNATIONAL_PAYMENT = 'INTERNATIONAL_PAYMENT'
    INTERNATIONAL_SCHEDULED_PAYMENT = 'INTERNATIONAL_SCHEDULED_PAYMENT'
    INTERNATIONAL_PERIODIC_PAYMENT = 'INTERNATIONAL_PERIODIC_PAYMENT'
    BULK_PAYMENT = 'BULK_PAYMENT'

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentTypeResponse":
        """Create an instance of PaymentTypeResponse from a JSON string"""
        return PaymentTypeResponse(json.loads(json_str))


