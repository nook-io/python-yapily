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


class AuthorisationStatus(str, Enum):
    """
    Current status of the embedded authorisation request in code form.
    """

    """
    allowed enum values
    """
    AWAITING_AUTHORIZATION = 'AWAITING_AUTHORIZATION'
    AWAITING_FURTHER_AUTHORIZATION = 'AWAITING_FURTHER_AUTHORIZATION'
    AWAITING_RE_AUTHORIZATION = 'AWAITING_RE_AUTHORIZATION'
    AUTHORIZED = 'AUTHORIZED'
    CONSUMED = 'CONSUMED'
    REJECTED = 'REJECTED'
    REVOKED = 'REVOKED'
    FAILED = 'FAILED'
    EXPIRED = 'EXPIRED'
    UNKNOWN = 'UNKNOWN'
    INVALID = 'INVALID'
    AWAITING_DECOUPLED_PRE_AUTHORIZATION = 'AWAITING_DECOUPLED_PRE_AUTHORIZATION'
    AWAITING_PRE_AUTHORIZATION = 'AWAITING_PRE_AUTHORIZATION'
    PRE_AUTHORIZED = 'PRE_AUTHORIZED'
    AWAITING_DECOUPLED_AUTHORIZATION = 'AWAITING_DECOUPLED_AUTHORIZATION'
    AWAITING_SCA_METHOD = 'AWAITING_SCA_METHOD'
    AWAITING_SCA_CODE = 'AWAITING_SCA_CODE'

    @classmethod
    def from_json(cls, json_str: str) -> "AuthorisationStatus":
        """Create an instance of AuthorisationStatus from a JSON string"""
        return AuthorisationStatus(json.loads(json_str))


