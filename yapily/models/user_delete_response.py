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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.consent_delete_response import ConsentDeleteResponse
from yapily.models.delete_status_enum import DeleteStatusEnum

class UserDeleteResponse(BaseModel):
    """
    Deletion of the user. Includes the user profile and all associate consents.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique identifier of the user.")
    delete_status: Optional[DeleteStatusEnum] = Field(None, alias="deleteStatus")
    creation_date: Optional[datetime] = Field(None, alias="creationDate", description="Date and time that the user was created.")
    user_consents: Optional[conlist(ConsentDeleteResponse, unique_items=True)] = Field(None, alias="userConsents")
    __properties = ["id", "deleteStatus", "creationDate", "userConsents"]

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
    def from_json(cls, json_str: str) -> UserDeleteResponse:
        """Create an instance of UserDeleteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in user_consents (list)
        _items = []
        if self.user_consents:
            for _item in self.user_consents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['userConsents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserDeleteResponse:
        """Create an instance of UserDeleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserDeleteResponse.parse_obj(obj)

        _obj = UserDeleteResponse.parse_obj({
            "id": obj.get("id"),
            "delete_status": obj.get("deleteStatus"),
            "creation_date": obj.get("creationDate"),
            "user_consents": [ConsentDeleteResponse.from_dict(_item) for _item in obj.get("userConsents")] if obj.get("userConsents") is not None else None
        })
        return _obj


