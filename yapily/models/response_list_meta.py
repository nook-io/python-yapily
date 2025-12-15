from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.pagination import Pagination
from typing import Set
from typing_extensions import Self


class ResponseListMeta(BaseModel):
    tracing_id: Optional[StrictStr] = Field(default=None, alias="tracingId")
    count: Optional[StrictInt] = None
    pagination: Optional[Pagination] = None
    __properties: ClassVar[List[str]] = ["tracingId", "count", "pagination"]
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
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "tracingId": obj.get("tracingId"),
                "count": obj.get("count"),
                "pagination": Pagination.from_dict(obj["pagination"])
                if obj.get("pagination") is not None
                else None,
            }
        )
        return _obj
