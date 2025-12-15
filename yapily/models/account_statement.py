from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class AccountStatement(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier for the statement."
    )
    start_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the statement period starts.",
        alias="startDateTime",
    )
    end_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the statement period ends.",
        alias="endDateTime",
    )
    creation_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the statement was created.",
        alias="creationDateTime",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "startDateTime",
        "endDateTime",
        "creationDateTime",
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
                "id": obj.get("id"),
                "startDateTime": obj.get("startDateTime"),
                "endDateTime": obj.get("endDateTime"),
                "creationDateTime": obj.get("creationDateTime"),
            }
        )
        return _obj
