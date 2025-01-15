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
from pydantic import BaseModel
from yapily.models.metadata import Metadata
from yapily.models.register_webhook201_response_data import (
    RegisterWebhook201ResponseData,
)


class RegisterWebhook201Response(BaseModel):
    """
    RegisterWebhook201Response
    """

    metadata: Optional[Metadata] = None
    data: Optional[RegisterWebhook201ResponseData] = None
    __properties = ["metadata", "data"]

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
    def from_json(cls, json_str: str) -> RegisterWebhook201Response:
        """Create an instance of RegisterWebhook201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegisterWebhook201Response:
        """Create an instance of RegisterWebhook201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterWebhook201Response.parse_obj(obj)

        _obj = RegisterWebhook201Response.parse_obj(
            {
                "metadata": Metadata.from_dict(obj.get("metadata"))
                if obj.get("metadata") is not None
                else None,
                "data": RegisterWebhook201ResponseData.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
            }
        )
        return _obj
