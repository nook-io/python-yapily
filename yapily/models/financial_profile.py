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
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.enriched_wrapper import EnrichedWrapper
from yapily.models.profile_consent import ProfileConsent


class FinancialProfile(BaseModel):
    """
    A financial profile for a User.  # noqa: E501
    """

    status: Optional[StrictStr] = Field(
        default=None,
        description="The status, can be EMPTY, PARTIAL, PENDING, COMPLETED or ERROR.",
    )
    profile_consents: Optional[conlist(ProfileConsent)] = Field(
        default=None,
        alias="profileConsents",
        description="A list of ProfileConsent used in the financial profile.",
    )
    enrichment: Optional[EnrichedWrapper] = None
    __properties = ["status", "profileConsents", "enrichment"]

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
    def from_json(cls, json_str: str) -> FinancialProfile:
        """Create an instance of FinancialProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in profile_consents (list)
        _items = []
        if self.profile_consents:
            for _item in self.profile_consents:
                if _item:
                    _items.append(_item.to_dict())
            _dict["profileConsents"] = _items
        # override the default output from pydantic by calling `to_dict()` of enrichment
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FinancialProfile:
        """Create an instance of FinancialProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FinancialProfile.parse_obj(obj)

        _obj = FinancialProfile.parse_obj(
            {
                "status": obj.get("status"),
                "profile_consents": [
                    ProfileConsent.from_dict(_item)
                    for _item in obj.get("profileConsents")
                ]
                if obj.get("profileConsents") is not None
                else None,
                "enrichment": EnrichedWrapper.from_dict(obj.get("enrichment"))
                if obj.get("enrichment") is not None
                else None,
            }
        )
        return _obj
