# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class ComplianceDataAddress(BaseModel):
    """
    This is the registered company or trading address of your end user.  # noqa: E501
    """

    address_line1: StrictStr = Field(
        default=...,
        alias="addressLine1",
        description="__Mandatory__. AddressLine1 of the business.",
    )
    address_line2: Optional[StrictStr] = Field(
        default=None,
        alias="addressLine2",
        description="__Optional__. AddressLine2 of the business.",
    )
    town_name: StrictStr = Field(
        default=...,
        alias="townName",
        description="__Mandatory__. Town name of the business.",
    )
    post_code: StrictStr = Field(
        default=...,
        alias="postCode",
        description="__Mandatory__. Post code of the business.",
    )
    country: StrictStr = Field(
        default=..., description="__Mandatory__. Country of the business."
    )
    __properties = ["addressLine1", "addressLine2", "townName", "postCode", "country"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ComplianceDataAddress:
        """Create an instance of ComplianceDataAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceDataAddress:
        """Create an instance of ComplianceDataAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataAddress.parse_obj(obj)

        _obj = ComplianceDataAddress.parse_obj(
            {
                "address_line1": obj.get("addressLine1"),
                "address_line2": obj.get("addressLine2"),
                "town_name": obj.get("townName"),
                "post_code": obj.get("postCode"),
                "country": obj.get("country"),
            }
        )
        return _obj
