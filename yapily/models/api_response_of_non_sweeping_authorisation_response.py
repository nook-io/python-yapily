from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.non_sweeping_authorisation_response import (
    NonSweepingAuthorisationResponse,
)
from yapily.models.raw_response import RawResponse
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_meta import ResponseMeta
from typing import Set
from typing_extensions import Self


class ApiResponseOfNonSweepingAuthorisationResponse(BaseModel):
    meta: Optional[ResponseMeta] = None
    data: Optional[NonSweepingAuthorisationResponse] = None
    links: Optional[Dict[str, StrictStr]] = None
    forwarded_data: Optional[List[ResponseForwardedData]] = Field(
        default=None, alias="forwardedData"
    )
    tracing_id: Optional[StrictStr] = Field(default=None, alias="tracingId")
    raw: Optional[List[RawResponse]] = None
    __properties: ClassVar[List[str]] = [
        "meta",
        "data",
        "links",
        "forwardedData",
        "tracingId",
        "raw",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        if self.data:
            _dict["data"] = self.data.to_dict()
        _items = []
        if self.forwarded_data:
            for _item_forwarded_data in self.forwarded_data:
                if _item_forwarded_data:
                    _items.append(_item_forwarded_data.to_dict())
            _dict["forwardedData"] = _items
        _items = []
        if self.raw:
            for _item_raw in self.raw:
                if _item_raw:
                    _items.append(_item_raw.to_dict())
            _dict["raw"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "meta": ResponseMeta.from_dict(obj["meta"])
                if obj.get("meta") is not None
                else None,
                "data": NonSweepingAuthorisationResponse.from_dict(obj["data"])
                if obj.get("data") is not None
                else None,
                "links": obj.get("links"),
                "forwardedData": [
                    ResponseForwardedData.from_dict(_item)
                    for _item in obj["forwardedData"]
                ]
                if obj.get("forwardedData") is not None
                else None,
                "tracingId": obj.get("tracingId"),
                "raw": [RawResponse.from_dict(_item) for _item in obj["raw"]]
                if obj.get("raw") is not None
                else None,
            }
        )
        return _obj
