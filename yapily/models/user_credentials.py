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

class UserCredentials(BaseModel):
    """
    __Conditional__. Used to capture the user's credentials to allow them to login to an `Institution` that uses the embedded account authorisation flow. <br><br>This is the first step required in the embedded account authorisation flow to authorise the `Consent`.  # noqa: E501
    """
    id: StrictStr = Field(..., description="__Mandatory__. The login id for the user for a particular `Institution`.")
    corporate_id: Optional[StrictStr] = Field(None, alias="corporateId", description="__Conditional__. The corporate login for the user for a particular corporate `Institution`.")
    password: StrictStr = Field(..., description="__Mandatory__. The password of the user to login to a particular `Institution`.")
    __properties = ["id", "corporateId", "password"]

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
    def from_json(cls, json_str: str) -> UserCredentials:
        """Create an instance of UserCredentials from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserCredentials:
        """Create an instance of UserCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserCredentials.parse_obj(obj)

        _obj = UserCredentials.parse_obj({
            "id": obj.get("id"),
            "corporate_id": obj.get("corporateId"),
            "password": obj.get("password")
        })
        return _obj


