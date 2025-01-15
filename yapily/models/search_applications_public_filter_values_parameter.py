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
from pydantic import BaseModel, Field, StrictStr, conint, conlist


class SearchApplicationsPublicFilterValuesParameter(BaseModel):
    """
    SearchApplicationsPublicFilterValuesParameter
    """

    application_ids: Optional[conlist(StrictStr, max_items=15)] = Field(
        default=None,
        alias="applicationIds",
        description="Sub-application ids to filter the results for. If provided, the results will only include sub-applications with the given ids. Non-existent ids will be ignored.",
    )
    offset: Optional[conint(strict=True, ge=0)] = Field(
        default=0, description="The number of results to skip."
    )
    limit: Optional[conint(strict=True, le=1000, ge=1)] = Field(
        default=1000, description="The maximum number of results to return."
    )
    sort: Optional[StrictStr] = Field(
        default="name",
        description="The field to sort the results by.<br><br>Possible values:<ul><li>`last_updated` (ascending)</li><li>`-last_updated` (descending)</li><li>`name` (ascending)</li><li>`-name` (descending)</li><li>`uuid` (ascending)</li><li>`-uuid` (descending)</li></ul>",
    )
    __properties = ["applicationIds", "offset", "limit", "sort"]

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
    def from_json(cls, json_str: str) -> SearchApplicationsPublicFilterValuesParameter:
        """Create an instance of SearchApplicationsPublicFilterValuesParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchApplicationsPublicFilterValuesParameter:
        """Create an instance of SearchApplicationsPublicFilterValuesParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchApplicationsPublicFilterValuesParameter.parse_obj(obj)

        _obj = SearchApplicationsPublicFilterValuesParameter.parse_obj(
            {
                "application_ids": obj.get("applicationIds"),
                "offset": obj.get("offset") if obj.get("offset") is not None else 0,
                "limit": obj.get("limit") if obj.get("limit") is not None else 1000,
                "sort": obj.get("sort") if obj.get("sort") is not None else "name",
            }
        )
        return _obj
