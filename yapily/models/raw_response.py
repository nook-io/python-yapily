from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.raw_request import RawRequest
from typing import Set
from typing_extensions import Self


class RawResponse(BaseModel):
    request: Optional[RawRequest] = None
    duration: Optional[StrictStr] = None
    headers: Optional[Dict[str, StrictStr]] = None
    result_code: Optional[StrictInt] = Field(default=None, alias="resultCode")
    result: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = [
        "request",
        "duration",
        "headers",
        "resultCode",
        "result",
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
        if self.request:
            _dict["request"] = self.request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "request": RawRequest.from_dict(obj["request"])
                if obj.get("request") is not None
                else None,
                "duration": obj.get("duration"),
                "headers": obj.get("headers"),
                "resultCode": obj.get("resultCode"),
                "result": obj.get("result"),
            }
        )
        return _obj
