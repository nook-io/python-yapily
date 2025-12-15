from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.filter_and_sort import FilterAndSort
from yapily.models.next import Next
from typing import Set
from typing_extensions import Self


class Pagination(BaseModel):
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    var_self: Optional[FilterAndSort] = Field(default=None, alias="self")
    next: Optional[Next] = None
    __properties: ClassVar[List[str]] = ["totalCount", "self", "next"]
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
        if self.var_self:
            _dict["self"] = self.var_self.to_dict()
        if self.next:
            _dict["next"] = self.next.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "totalCount": obj.get("totalCount"),
                "self": FilterAndSort.from_dict(obj["self"])
                if obj.get("self") is not None
                else None,
                "next": Next.from_dict(obj["next"])
                if obj.get("next") is not None
                else None,
            }
        )
        return _obj
