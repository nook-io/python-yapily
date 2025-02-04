# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import json
import re  # noqa: F401

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
