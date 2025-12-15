from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self


class FundsAvailable(BaseModel):
    funds_available: StrictBool = Field(
        description="__Mandatory__. Indicates whether funds are available or not.",
        alias="fundsAvailable",
    )
    funds_available_at: datetime = Field(
        description="__Mandatory__. Date and Time when the funds availability is checked.",
        alias="fundsAvailableAt",
    )
    __properties: ClassVar[List[str]] = ["fundsAvailable", "fundsAvailableAt"]
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
                "fundsAvailable": obj.get("fundsAvailable"),
                "fundsAvailableAt": obj.get("fundsAvailableAt"),
            }
        )
        return _obj
