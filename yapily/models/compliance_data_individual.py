from __future__ import annotations
import pprint
import json
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self


class ComplianceDataIndividual(BaseModel):
    name: StrictStr = Field(
        description="This is the first and last name of your end user."
    )
    birth_date: date = Field(
        description="This is the date of birth of your end user.", alias="birthDate"
    )
    __properties: ClassVar[List[str]] = ["name", "birthDate"]
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
            {"name": obj.get("name"), "birthDate": obj.get("birthDate")}
        )
        return _obj
