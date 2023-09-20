# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.country import Country
from yapily.models.credentials_type import CredentialsType
from yapily.models.environment_type import EnvironmentType
from yapily.models.feature_enum import FeatureEnum
from yapily.models.media import Media
from yapily.models.monitoring_feature_status import MonitoringFeatureStatus

class Institution(BaseModel):
    """
    Institution
    """
    id: Optional[StrictStr] = Field(None, description="The Yapily Id for the `Institution`")
    name: Optional[StrictStr] = Field(None, description="The friendly name of the `Institution`")
    full_name: Optional[StrictStr] = Field(None, alias="fullName", description="The full name of the `Institution`")
    countries: Optional[conlist(Country, unique_items=True)] = Field(None, description="An array of `Country` denoting which regions the `Institution` provides coverage for")
    environment_type: Optional[EnvironmentType] = Field(None, alias="environmentType")
    credentials_type: Optional[CredentialsType] = Field(None, alias="credentialsType")
    media: Optional[conlist(Media, unique_items=True)] = Field(None, description="Contains links to the logo and the icons for the `Institution`")
    features: Optional[conlist(FeatureEnum, unique_items=True)] = None
    monitoring: Optional[Dict[str, MonitoringFeatureStatus]] = None
    __properties = ["id", "name", "fullName", "countries", "environmentType", "credentialsType", "media", "features", "monitoring"]

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
    def from_json(cls, json_str: str) -> Institution:
        """Create an instance of Institution from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in countries (list)
        _items = []
        if self.countries:
            for _item in self.countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['countries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item in self.media:
                if _item:
                    _items.append(_item.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in monitoring (dict)
        _field_dict = {}
        if self.monitoring:
            for _key in self.monitoring:
                if self.monitoring[_key]:
                    _field_dict[_key] = self.monitoring[_key].to_dict()
            _dict['monitoring'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Institution:
        """Create an instance of Institution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Institution.parse_obj(obj)

        _obj = Institution.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "full_name": obj.get("fullName"),
            "countries": [Country.from_dict(_item) for _item in obj.get("countries")] if obj.get("countries") is not None else None,
            "environment_type": obj.get("environmentType"),
            "credentials_type": obj.get("credentialsType"),
            "media": [Media.from_dict(_item) for _item in obj.get("media")] if obj.get("media") is not None else None,
            "features": obj.get("features"),
            "monitoring": dict(
                (_k, MonitoringFeatureStatus.from_dict(_v))
                for _k, _v in obj.get("monitoring").items()
            )
            if obj.get("monitoring") is not None
            else None
        })
        return _obj


