# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PaymentStatus(str, Enum):
    """
    The status of the Payment. <br><br>For more information, see [Payment Status](/guides/payments/payment-status/)
    """

    """
    allowed enum values
    """
    PENDING = 'PENDING'
    FAILED = 'FAILED'
    DECLINED = 'DECLINED'
    COMPLETED = 'COMPLETED'
    COMPLETED_SETTLEMENT_IN_PROCESS = 'COMPLETED_SETTLEMENT_IN_PROCESS'
    EXPIRED = 'EXPIRED'
    UNKNOWN = 'UNKNOWN'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    @classmethod
    def from_json(cls, json_str: str) -> PaymentStatus:
        """Create an instance of PaymentStatus from a JSON string"""
        return PaymentStatus(json.loads(json_str))


