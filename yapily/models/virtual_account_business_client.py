# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
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
from yapily.models.virtual_account_address import VirtualAccountAddress
from yapily.models.virtual_account_client_business_type import VirtualAccountClientBusinessType

class VirtualAccountBusinessClient(BaseModel):
    """
    VirtualAccountBusinessClient
    """
    name: StrictStr = Field(...)
    type: VirtualAccountClientBusinessType = Field(...)
    registration_number: StrictStr = Field(..., alias="registrationNumber")
    registered_address: VirtualAccountAddress = Field(..., alias="registeredAddress")
    trading_address: Optional[VirtualAccountAddress] = Field(None, alias="tradingAddress")
    contact_name: StrictStr = Field(..., alias="contactName")
    email: StrictStr = Field(...)
    phone: StrictStr = Field(...)
    __properties = ["name", "type", "registrationNumber", "registeredAddress", "tradingAddress", "contactName", "email", "phone"]

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
    def from_json(cls, json_str: str) -> VirtualAccountBusinessClient:
        """Create an instance of VirtualAccountBusinessClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of registered_address
        if self.registered_address:
            _dict['registeredAddress'] = self.registered_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trading_address
        if self.trading_address:
            _dict['tradingAddress'] = self.trading_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VirtualAccountBusinessClient:
        """Create an instance of VirtualAccountBusinessClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VirtualAccountBusinessClient.parse_obj(obj)

        _obj = VirtualAccountBusinessClient.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "registration_number": obj.get("registrationNumber"),
            "registered_address": VirtualAccountAddress.from_dict(obj.get("registeredAddress")) if obj.get("registeredAddress") is not None else None,
            "trading_address": VirtualAccountAddress.from_dict(obj.get("tradingAddress")) if obj.get("tradingAddress") is not None else None,
            "contact_name": obj.get("contactName"),
            "email": obj.get("email"),
            "phone": obj.get("phone")
        })
        return _obj


