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

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.virtual_account_beneficiary_account import VirtualAccountBeneficiaryAccount
from yapily.models.virtual_account_beneficiary_address import VirtualAccountBeneficiaryAddress

class VirtualAccountBeneficiaryRequest(BaseModel):
    """
    VirtualAccountBeneficiaryRequest
    """
    nickname: StrictStr = Field(..., description="Reference that can be provided in order to help with identification of the Beneficiary")
    type: StrictStr = Field(..., description="Indicates the type of Beneficiary as either an INDIVIDUAL or BUSINESS")
    name: StrictStr = Field(...)
    birth_date: Optional[date] = Field(None, alias="birthDate")
    payment_schemes: conlist(StrictStr) = Field(..., alias="paymentSchemes", description="Beneficiary payment schemes")
    address: VirtualAccountBeneficiaryAddress = Field(...)
    account: VirtualAccountBeneficiaryAccount = Field(...)
    __properties = ["nickname", "type", "name", "birthDate", "paymentSchemes", "address", "account"]

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
    def from_json(cls, json_str: str) -> VirtualAccountBeneficiaryRequest:
        """Create an instance of VirtualAccountBeneficiaryRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VirtualAccountBeneficiaryRequest:
        """Create an instance of VirtualAccountBeneficiaryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VirtualAccountBeneficiaryRequest.parse_obj(obj)

        _obj = VirtualAccountBeneficiaryRequest.parse_obj({
            "nickname": obj.get("nickname"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "birth_date": obj.get("birthDate"),
            "payment_schemes": obj.get("paymentSchemes"),
            "address": VirtualAccountBeneficiaryAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "account": VirtualAccountBeneficiaryAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None
        })
        return _obj


