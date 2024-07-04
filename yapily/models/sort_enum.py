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


class SortEnum(str, Enum):
    """
    The attribute on which resources / records returned should be sorted. Valid options for the sort parameter.
    """

    """
    allowed enum values
    """
    DATE = 'date'
    MINUS_DATE = '-date'

    @classmethod
    def from_json(cls, json_str: str) -> "SortEnum":
        """Create an instance of SortEnum from a JSON string"""
        return SortEnum(json.loads(json_str))


