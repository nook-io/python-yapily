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
from yapily.models.api_list_response_of_real_time_transaction_links import (
    ApiListResponseOfRealTimeTransactionLinks,
)
from yapily.models.raw_response import RawResponse
from yapily.models.real_time_transaction import RealTimeTransaction
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_meta_with_count import ResponseMetaWithCount


class ApiListResponseOfRealTimeTransaction(BaseModel):
    """
    ApiListResponseOfRealTimeTransaction
    """

    meta: Optional[ResponseMetaWithCount] = None
    data: Optional[conlist(RealTimeTransaction)] = None
    links: Optional[ApiListResponseOfRealTimeTransactionLinks] = None
    forwarded_data: Optional[conlist(ResponseForwardedData)] = Field(
        default=None, alias="forwardedData"
    )
    raw: Optional[conlist(RawResponse)] = None
    tracing_id: Optional[StrictStr] = Field(default=None, alias="tracingId")
    __properties = ["meta", "data", "links", "forwardedData", "raw", "tracingId"]

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
    def from_json(cls, json_str: str) -> ApiListResponseOfRealTimeTransaction:
        """Create an instance of ApiListResponseOfRealTimeTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data"] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict["links"] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in forwarded_data (list)
        _items = []
        if self.forwarded_data:
            for _item in self.forwarded_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["forwardedData"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item in self.raw:
                if _item:
                    _items.append(_item.to_dict())
            _dict["raw"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiListResponseOfRealTimeTransaction:
        """Create an instance of ApiListResponseOfRealTimeTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiListResponseOfRealTimeTransaction.parse_obj(obj)

        _obj = ApiListResponseOfRealTimeTransaction.parse_obj(
            {
                "meta": ResponseMetaWithCount.from_dict(obj.get("meta"))
                if obj.get("meta") is not None
                else None,
                "data": [
                    RealTimeTransaction.from_dict(_item) for _item in obj.get("data")
                ]
                if obj.get("data") is not None
                else None,
                "links": ApiListResponseOfRealTimeTransactionLinks.from_dict(
                    obj.get("links")
                )
                if obj.get("links") is not None
                else None,
                "forwarded_data": [
                    ResponseForwardedData.from_dict(_item)
                    for _item in obj.get("forwardedData")
                ]
                if obj.get("forwardedData") is not None
                else None,
                "raw": [RawResponse.from_dict(_item) for _item in obj.get("raw")]
                if obj.get("raw") is not None
                else None,
                "tracing_id": obj.get("tracingId"),
            }
        )
        return _obj
