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





class MonitoringStatusEnum(str, Enum):
    """
    The latest operational status.
    """

    """
    allowed enum values
    """
    UP = 'Up'
    DOWN = 'Down'
    WARNING = 'Warning'
    UNKNOWN = 'Unknown'
    EXPIRED = 'Expired'

    @classmethod
    def from_json(cls, json_str: str) -> MonitoringStatusEnum:
        """Create an instance of MonitoringStatusEnum from a JSON string"""
        return MonitoringStatusEnum(json.loads(json_str))


