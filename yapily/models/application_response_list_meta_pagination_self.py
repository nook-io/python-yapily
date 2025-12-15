from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self


class ApplicationResponseListMetaPaginationSelf(BaseModel):
    offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, description="The number of skipped applications."
    )
    limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="The maximum number of applications for the current page.",
    )
    sort: Optional[StrictStr] = Field(
        default=None,
        description='The field by which results are sorted by. Default direction is ascending, descending is identified by a "-" prefix.',
    )
    __properties: ClassVar[List[str]] = ["offset", "limit", "sort"]
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
                "offset": obj.get("offset"),
                "limit": obj.get("limit"),
                "sort": obj.get("sort"),
            }
        )
        return _obj
