from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class RawRequest(BaseModel):
    method: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    request_instant: Optional[datetime] = Field(default=None, alias="requestInstant")
    headers: Optional[Dict[str, StrictStr]] = None
    body: Optional[Dict[str, Any]] = None
    body_parameters: Optional[Dict[str, StrictStr]] = Field(
        default=None, alias="bodyParameters"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    __properties: ClassVar[List[str]] = [
        "method",
        "url",
        "requestInstant",
        "headers",
        "body",
        "bodyParameters",
        "startTime",
        "startedAt",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "method": obj.get("method"),
                "url": obj.get("url"),
                "requestInstant": obj.get("requestInstant"),
                "headers": obj.get("headers"),
                "body": obj.get("body"),
                "bodyParameters": obj.get("bodyParameters"),
                "startTime": obj.get("startTime"),
                "startedAt": obj.get("startedAt"),
            }
        )
        return _obj
