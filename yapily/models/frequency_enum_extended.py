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


class FrequencyEnumExtended(str, Enum):
    """
    __Mandatory__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information
    """

    """
    allowed enum values
    """
    DAILY = 'DAILY'
    EVERY_WORKING_DAY = 'EVERY_WORKING_DAY'
    CALENDAR_DAY = 'CALENDAR_DAY'
    WEEKLY = 'WEEKLY'
    EVERY_TWO_WEEKS = 'EVERY_TWO_WEEKS'
    MONTHLY = 'MONTHLY'
    EVERY_TWO_MONTHS = 'EVERY_TWO_MONTHS'
    QUARTERLY = 'QUARTERLY'
    SEMIANNUAL = 'SEMIANNUAL'
    ANNUAL = 'ANNUAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FrequencyEnumExtended from a JSON string"""
        return cls(json.loads(json_str))


