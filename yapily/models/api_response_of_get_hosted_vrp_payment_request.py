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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.hosted_vrp_payment_response import HostedVRPPaymentResponse
from yapily.models.response_meta import ResponseMeta

class ApiResponseOfGetHostedVRPPaymentRequest(BaseModel):
    """
    ApiResponseOfGetHostedVRPPaymentRequest
    """
    meta: Optional[ResponseMeta] = None
    data: Optional[HostedVRPPaymentResponse] = None
    tracing_id: Optional[StrictStr] = Field(None, alias="tracingId")
    __properties = ["meta", "data", "tracingId"]

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
    def from_json(cls, json_str: str) -> ApiResponseOfGetHostedVRPPaymentRequest:
        """Create an instance of ApiResponseOfGetHostedVRPPaymentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiResponseOfGetHostedVRPPaymentRequest:
        """Create an instance of ApiResponseOfGetHostedVRPPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResponseOfGetHostedVRPPaymentRequest.parse_obj(obj)

        _obj = ApiResponseOfGetHostedVRPPaymentRequest.parse_obj({
            "meta": ResponseMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
            "data": HostedVRPPaymentResponse.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "tracing_id": obj.get("tracingId")
        })
        return _obj


