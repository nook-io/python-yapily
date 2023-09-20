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





class ChargeBearerType(str, Enum):
    """
    __Optional__. Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Valid values are:<ul><li>`DEBT` - All transaction charges are to be borne by the debtor.</li><li>`CRED` - All transaction charges are to be borne by the creditor.</li><li>`SHAR` - In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor</li><li>`SLEV` - Charges are to be applied following the rules agreed in the service level and/or scheme.</li></ul>
    """

    """
    allowed enum values
    """
    DEBT = 'DEBT'
    CRED = 'CRED'
    SHAR = 'SHAR'
    SLEV = 'SLEV'

    @classmethod
    def from_json(cls, json_str: str) -> ChargeBearerType:
        """Create an instance of ChargeBearerType from a JSON string"""
        return ChargeBearerType(json.loads(json_str))


