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
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class EnrichmentMerchant(BaseModel):
    """
    EnrichmentMerchant
    """
    merchant_name: Optional[StrictStr] = Field(None, alias="merchantName")
    parent_group: Optional[StrictStr] = Field(None, alias="parentGroup")
    __properties = ["merchantName", "parentGroup"]

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
    def from_json(cls, json_str: str) -> EnrichmentMerchant:
        """Create an instance of EnrichmentMerchant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnrichmentMerchant:
        """Create an instance of EnrichmentMerchant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichmentMerchant.parse_obj(obj)

        _obj = EnrichmentMerchant.parse_obj({
            "merchant_name": obj.get("merchantName"),
            "parent_group": obj.get("parentGroup")
        })
        return _obj


