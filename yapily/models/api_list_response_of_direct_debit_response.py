# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.direct_debit_response import DirectDebitResponse
from yapily.models.filtered_client_payload_list_direct_debit_response import FilteredClientPayloadListDirectDebitResponse
from yapily.models.raw_response import RawResponse
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_list_meta import ResponseListMeta

class ApiListResponseOfDirectDebitResponse(BaseModel):
    """
    ApiListResponseOfDirectDebitResponse
    """
    meta: Optional[ResponseListMeta] = None
    data: Optional[conlist(DirectDebitResponse)] = None
    links: Optional[Dict[str, StrictStr]] = None
    forwarded_data: Optional[conlist(ResponseForwardedData)] = Field(None, alias="forwardedData")
    raw: Optional[conlist(RawResponse)] = None
    paging: Optional[FilteredClientPayloadListDirectDebitResponse] = None
    tracing_id: Optional[StrictStr] = Field(None, alias="tracingId")
    __properties = ["meta", "data", "links", "forwardedData", "raw", "paging", "tracingId"]

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
    def from_json(cls, json_str: str) -> ApiListResponseOfDirectDebitResponse:
        """Create an instance of ApiListResponseOfDirectDebitResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in forwarded_data (list)
        _items = []
        if self.forwarded_data:
            for _item in self.forwarded_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['forwardedData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item in self.raw:
                if _item:
                    _items.append(_item.to_dict())
            _dict['raw'] = _items
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict['paging'] = self.paging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiListResponseOfDirectDebitResponse:
        """Create an instance of ApiListResponseOfDirectDebitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiListResponseOfDirectDebitResponse.parse_obj(obj)

        _obj = ApiListResponseOfDirectDebitResponse.parse_obj({
            "meta": ResponseListMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
            "data": [DirectDebitResponse.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "links": obj.get("links"),
            "forwarded_data": [ResponseForwardedData.from_dict(_item) for _item in obj.get("forwardedData")] if obj.get("forwardedData") is not None else None,
            "raw": [RawResponse.from_dict(_item) for _item in obj.get("raw")] if obj.get("raw") is not None else None,
            "paging": FilteredClientPayloadListDirectDebitResponse.from_dict(obj.get("paging")) if obj.get("paging") is not None else None,
            "tracing_id": obj.get("tracingId")
        })
        return _obj


