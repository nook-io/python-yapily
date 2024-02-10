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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from yapily.models.links import Links
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_list_meta import ResponseListMeta
from yapily.models.virtual_account_client import VirtualAccountClient
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiListResponseOfVirtualAccountClient(BaseModel):
    """
    ApiListResponseOfVirtualAccountClient
    """ # noqa: E501
    meta: Optional[ResponseListMeta] = None
    data: Optional[List[VirtualAccountClient]] = None
    links: Optional[Links] = None
    forwarded_data: Optional[List[ResponseForwardedData]] = Field(default=None, alias="forwardedData")
    tracing_id: Optional[StrictStr] = Field(default=None, alias="tracingId")
    __properties: ClassVar[List[str]] = ["meta", "data", "links", "forwardedData", "tracingId"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiListResponseOfVirtualAccountClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in forwarded_data (list)
        _items = []
        if self.forwarded_data:
            for _item in self.forwarded_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['forwardedData'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiListResponseOfVirtualAccountClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": ResponseListMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
            "data": [VirtualAccountClient.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "links": Links.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "forwardedData": [ResponseForwardedData.from_dict(_item) for _item in obj.get("forwardedData")] if obj.get("forwardedData") is not None else None,
            "tracingId": obj.get("tracingId")
        })
        return _obj


