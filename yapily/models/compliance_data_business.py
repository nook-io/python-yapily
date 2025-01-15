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
from yapily.models.compliance_data_address import ComplianceDataAddress


class ComplianceDataBusiness(BaseModel):
    """
    __Conditional__. Mandatory if the type is BUSINESS.  # noqa: E501
    """

    name: StrictStr = Field(
        default=..., description="This is the registered company name of your end user."
    )
    registration_number: StrictStr = Field(
        default=...,
        alias="registrationNumber",
        description="This is the registered company number of the business.",
    )
    registered_address: ComplianceDataAddress = Field(
        default=..., alias="registeredAddress"
    )
    trading_address: Optional[ComplianceDataAddress] = Field(
        default=None, alias="tradingAddress"
    )
    __properties = ["name", "registrationNumber", "registeredAddress", "tradingAddress"]

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
    def from_json(cls, json_str: str) -> ComplianceDataBusiness:
        """Create an instance of ComplianceDataBusiness from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of registered_address
        if self.registered_address:
            _dict["registeredAddress"] = self.registered_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trading_address
        if self.trading_address:
            _dict["tradingAddress"] = self.trading_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceDataBusiness:
        """Create an instance of ComplianceDataBusiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataBusiness.parse_obj(obj)

        _obj = ComplianceDataBusiness.parse_obj(
            {
                "name": obj.get("name"),
                "registration_number": obj.get("registrationNumber"),
                "registered_address": ComplianceDataAddress.from_dict(
                    obj.get("registeredAddress")
                )
                if obj.get("registeredAddress") is not None
                else None,
                "trading_address": ComplianceDataAddress.from_dict(
                    obj.get("tradingAddress")
                )
                if obj.get("tradingAddress") is not None
                else None,
            }
        )
        return _obj
