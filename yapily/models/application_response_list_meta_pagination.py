from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from yapily.models.application_response_list_meta_pagination_self import (
    ApplicationResponseListMetaPaginationSelf,
)
from typing import Set
from typing_extensions import Self


class ApplicationResponseListMetaPagination(BaseModel):
    var_self: Optional[ApplicationResponseListMetaPaginationSelf] = Field(
        default=None, alias="self"
    )
    total_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="The total number of applications that match the given filter.",
        alias="totalCount",
    )
    __properties: ClassVar[List[str]] = ["self", "totalCount"]
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "self": ApplicationResponseListMetaPaginationSelf.from_dict(obj["self"])
                if obj.get("self") is not None
                else None,
                "totalCount": obj.get("totalCount"),
            }
        )
        return _obj
