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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.account_identification_response import AccountIdentificationResponse
from yapily.models.address_response import AddressResponse

class PayeeDetailsResponse(BaseModel):
    """
     Details of the beneficiary [person or business].  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="The account holder name of the beneficiary.")
    account_identifications: Optional[conlist(AccountIdentificationResponse, unique_items=True)] = Field(None, alias="accountIdentifications", description="The account identifications that identify the `Payee` bank account.")
    address: Optional[AddressResponse] = None
    merchant_id: Optional[StrictStr] = Field(None, alias="merchantId", description="The merchant ID is a unique code provided by the payment processor to the merchant.")
    merchant_category_code: Optional[StrictStr] = Field(None, alias="merchantCategoryCode", description="The category code of the merchant in case the `Payee` is a business. Specified as a 3-letter ISO 18245 code.")
    __properties = ["name", "accountIdentifications", "address", "merchantId", "merchantCategoryCode"]

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
    def from_json(cls, json_str: str) -> PayeeDetailsResponse:
        """Create an instance of PayeeDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifications (list)
        _items = []
        if self.account_identifications:
            for _item in self.account_identifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountIdentifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayeeDetailsResponse:
        """Create an instance of PayeeDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayeeDetailsResponse.parse_obj(obj)

        _obj = PayeeDetailsResponse.parse_obj({
            "name": obj.get("name"),
            "account_identifications": [AccountIdentificationResponse.from_dict(_item) for _item in obj.get("accountIdentifications")] if obj.get("accountIdentifications") is not None else None,
            "address": AddressResponse.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "merchant_id": obj.get("merchantId"),
            "merchant_category_code": obj.get("merchantCategoryCode")
        })
        return _obj

