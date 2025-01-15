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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.delete_status_enum import DeleteStatusEnum


class ConsentDeleteResponse(BaseModel):
    """
    ConsentDeleteResponse
    """

    id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. User-friendly identifier of the `User` that provides authorisation. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
    )
    delete_status: Optional[DeleteStatusEnum] = Field(
        default=None, alias="deleteStatus"
    )
    institution_id: Optional[StrictStr] = Field(
        default=None,
        alias="institutionId",
        description="__Mandatory__. The `Institution` the authorisation request is sent to.",
    )
    institution_consent_id: Optional[StrictStr] = Field(
        default=None,
        alias="institutionConsentId",
        description="Identification of the consent at the Institution.",
    )
    creation_date: Optional[datetime] = Field(
        default=None,
        alias="creationDate",
        description="Date and time of when the consent was authorised.",
    )
    __properties = [
        "id",
        "deleteStatus",
        "institutionId",
        "institutionConsentId",
        "creationDate",
    ]

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
    def from_json(cls, json_str: str) -> ConsentDeleteResponse:
        """Create an instance of ConsentDeleteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConsentDeleteResponse:
        """Create an instance of ConsentDeleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConsentDeleteResponse.parse_obj(obj)

        _obj = ConsentDeleteResponse.parse_obj(
            {
                "id": obj.get("id"),
                "delete_status": obj.get("deleteStatus"),
                "institution_id": obj.get("institutionId"),
                "institution_consent_id": obj.get("institutionConsentId"),
                "creation_date": obj.get("creationDate"),
            }
        )
        return _obj
