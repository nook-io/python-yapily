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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from yapily.models.filter_and_sort import FilterAndSort
from yapily.models.institution import Institution


class FilteredClientPayloadListInstitution(BaseModel):
    """
    FilteredClientPayloadListInstitution
    """

    api_call: Optional[Dict[str, Any]] = Field(default=None, alias="apiCall")
    data: Optional[conlist(Institution)] = None
    next_cursor_hash: Optional[StrictStr] = Field(default=None, alias="nextCursorHash")
    next_link: Optional[StrictStr] = Field(default=None, alias="nextLink")
    paging_map: Optional[Dict[str, FilterAndSort]] = Field(
        default=None, alias="pagingMap"
    )
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    __properties = [
        "apiCall",
        "data",
        "nextCursorHash",
        "nextLink",
        "pagingMap",
        "totalCount",
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
    def from_json(cls, json_str: str) -> FilteredClientPayloadListInstitution:
        """Create an instance of FilteredClientPayloadListInstitution from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data"] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in paging_map (dict)
        _field_dict = {}
        if self.paging_map:
            for _key in self.paging_map:
                if self.paging_map[_key]:
                    _field_dict[_key] = self.paging_map[_key].to_dict()
            _dict["pagingMap"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilteredClientPayloadListInstitution:
        """Create an instance of FilteredClientPayloadListInstitution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilteredClientPayloadListInstitution.parse_obj(obj)

        _obj = FilteredClientPayloadListInstitution.parse_obj(
            {
                "api_call": obj.get("apiCall"),
                "data": [Institution.from_dict(_item) for _item in obj.get("data")]
                if obj.get("data") is not None
                else None,
                "next_cursor_hash": obj.get("nextCursorHash"),
                "next_link": obj.get("nextLink"),
                "paging_map": dict(
                    (_k, FilterAndSort.from_dict(_v))
                    for _k, _v in obj.get("pagingMap").items()
                )
                if obj.get("pagingMap") is not None
                else None,
                "total_count": obj.get("totalCount"),
            }
        )
        return _obj
