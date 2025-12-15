from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.type import Type
from typing import Set
from typing_extensions import Self


class ScaMethod(BaseModel):
    id: StrictStr = Field(
        description="__Mandatory__. The id of the sca method provided by the `Institution`"
    )
    type: Optional[Type] = None
    description: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. A description of the sca method if provided by the `Institution`",
    )
    information: Optional[StrictStr] = Field(
        default=None,
        description="Additional information from the institution to provide to the PSU to help with the selected SCA method. The language is determined by the institution and may vary.",
    )
    data: Optional[List[StrictStr]] = Field(
        default=None,
        description="Data from the institution to provide to the PSU to complete authorisation. The language is determined by the institution and may vary.",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "type",
        "description",
        "information",
        "data",
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
                "type": obj.get("type"),
                "description": obj.get("description"),
                "information": obj.get("information"),
                "data": obj.get("data"),
            }
        )
        return _obj
