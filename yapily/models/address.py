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
from yapily.models.address_type_enum import AddressTypeEnum

class Address(BaseModel):
    """
    __Conditional__. The address of the `Payee` or `Payer`.<ul><li>`payee.address` is mandatory when the `paymentType` is an `INTERNATIONAL` payment</li><li>An `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to make a payment.</li></ul>  # noqa: E501
    """
    address_lines: Optional[conlist(StrictStr)] = Field(None, alias="addressLines", description="__Optional__. The address line of the address")
    street_name: Optional[StrictStr] = Field(None, alias="streetName", description="__Optional__. The street name of the address")
    building_number: Optional[StrictStr] = Field(None, alias="buildingNumber", description="__Optional__. The building number of the address")
    post_code: Optional[StrictStr] = Field(None, alias="postCode", description="__Optional__. The post code of the address")
    town_name: Optional[StrictStr] = Field(None, alias="townName", description="__Optional__. The town name of the address")
    county: Optional[conlist(StrictStr)] = Field(None, description="__Optional__. The list of counties for the address")
    country: Optional[StrictStr] = Field(None, description="__Conditional__. The 2-letter country code for the address. <br><br>An `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to make a payment")
    department: Optional[StrictStr] = Field(None, description="__Optional__. The department for the address")
    sub_department: Optional[StrictStr] = Field(None, alias="subDepartment", description="__Optional__. The sub-department for the address")
    address_type: Optional[AddressTypeEnum] = Field(None, alias="addressType")
    __properties = ["addressLines", "streetName", "buildingNumber", "postCode", "townName", "county", "country", "department", "subDepartment", "addressType"]

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
    def from_json(cls, json_str: str) -> Address:
        """Create an instance of Address from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Address:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Address.parse_obj(obj)

        _obj = Address.parse_obj({
            "address_lines": obj.get("addressLines"),
            "street_name": obj.get("streetName"),
            "building_number": obj.get("buildingNumber"),
            "post_code": obj.get("postCode"),
            "town_name": obj.get("townName"),
            "county": obj.get("county"),
            "country": obj.get("country"),
            "department": obj.get("department"),
            "sub_department": obj.get("subDepartment"),
            "address_type": obj.get("addressType")
        })
        return _obj


