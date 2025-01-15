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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.payment_authorisation_request_response import PaymentAuthorisationRequestResponse
from yapily.models.raw_response import RawResponse
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_meta import ResponseMeta
from typing import Optional, Set
from typing_extensions import Self

class ApiResponseOfPaymentAuthorisationRequestResponse(BaseModel):
    """
    ApiResponseOfPaymentAuthorisationRequestResponse
    """ # noqa: E501
    meta: Optional[ResponseMeta] = None
    data: Optional[PaymentAuthorisationRequestResponse] = None
    links: Optional[Dict[str, StrictStr]] = None
    forwarded_data: Optional[List[ResponseForwardedData]] = Field(default=None, alias="forwardedData")
    raw: Optional[List[RawResponse]] = None
    tracing_id: Optional[StrictStr] = Field(default=None, alias="tracingId")
    __properties: ClassVar[List[str]] = ["meta", "data", "links", "forwardedData", "raw", "tracingId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiResponseOfPaymentAuthorisationRequestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in forwarded_data (list)
        _items = []
        if self.forwarded_data:
            for _item_forwarded_data in self.forwarded_data:
                if _item_forwarded_data:
                    _items.append(_item_forwarded_data.to_dict())
            _dict['forwardedData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item_raw in self.raw:
                if _item_raw:
                    _items.append(_item_raw.to_dict())
            _dict['raw'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiResponseOfPaymentAuthorisationRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": ResponseMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "data": PaymentAuthorisationRequestResponse.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "links": obj.get("links"),
            "forwardedData": [ResponseForwardedData.from_dict(_item) for _item in obj["forwardedData"]] if obj.get("forwardedData") is not None else None,
            "raw": [RawResponse.from_dict(_item) for _item in obj["raw"]] if obj.get("raw") is not None else None,
            "tracingId": obj.get("tracingId")
        })
        return _obj


