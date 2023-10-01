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
from yapily.models.type import Type

class ScaMethod(BaseModel):
    """
    __Conditional__. Used to update the authorisation with the sca method of the user's choice for the `Institution` that uses the embedded authorisation flow. If the user has multiple sca methods configured, the `Institution` will allow the user to select from each of these options. <br><br>When the user has multiple sca methods for the `Institution`, this is the second step required in the embedded authorisation flow to authorise the `Consent`.  # noqa: E501
    """
    id: StrictStr = Field(..., description="__Mandatory__. The id of the sca method provided by the `Institution`")
    type: Optional[Type] = None
    description: Optional[StrictStr] = Field(None, description="__Optional__. A description of the sca method if provided by the `Institution`")
    information: Optional[StrictStr] = Field(None, description="Additional information from the institution to provide to the PSU to help with the selected SCA method. The language is determined by the institution and may vary.")
    data: Optional[conlist(StrictStr)] = Field(None, description="Data from the institution to provide to the PSU to complete authorisation. The language is determined by the institution and may vary.")
    __properties = ["id", "type", "description", "information", "data"]

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
    def from_json(cls, json_str: str) -> ScaMethod:
        """Create an instance of ScaMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScaMethod:
        """Create an instance of ScaMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScaMethod.parse_obj(obj)

        _obj = ScaMethod.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "information": obj.get("information"),
            "data": obj.get("data")
        })
        return _obj


