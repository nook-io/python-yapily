# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TransactionStatusEnum(str, Enum):
    """
    TransactionStatusEnum
    """

    """
    allowed enum values
    """
    BOOKED = 'BOOKED'
    PENDING = 'PENDING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


