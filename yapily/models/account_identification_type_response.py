# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AccountIdentificationTypeResponse(str, Enum):
    """
    Used to describe the format of the account.<br><br> See [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#account-identifications-combinations) for more information.
    """

    """
    allowed enum values
    """
    SORT_CODE = 'SORT_CODE'
    ACCOUNT_NUMBER = 'ACCOUNT_NUMBER'
    IBAN = 'IBAN'
    BBAN = 'BBAN'
    BIC = 'BIC'
    PAN = 'PAN'
    MASKED_PAN = 'MASKED_PAN'
    MSISDN = 'MSISDN'
    BSB = 'BSB'
    NCC = 'NCC'
    ABA = 'ABA'
    ABA_WIRE = 'ABA_WIRE'
    ABA_ACH = 'ABA_ACH'
    EMAIL = 'EMAIL'
    ROLL_NUMBER = 'ROLL_NUMBER'
    BLZ = 'BLZ'
    IFS = 'IFS'
    CLABE = 'CLABE'
    CTN = 'CTN'
    BRANCH_CODE = 'BRANCH_CODE'
    VIRTUAL_ACCOUNT_ID = 'VIRTUAL_ACCOUNT_ID'

    @classmethod
    def from_json(cls, json_str: str) -> AccountIdentificationTypeResponse:
        """Create an instance of AccountIdentificationTypeResponse from a JSON string"""
        return AccountIdentificationTypeResponse(json.loads(json_str))


