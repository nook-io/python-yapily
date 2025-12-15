from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.frequency_enum_extended import FrequencyEnumExtended
from typing import Set
from typing_extensions import Self


class FrequencyResponse(BaseModel):
    frequency_type: Optional[FrequencyEnumExtended] = Field(
        default=None, alias="frequencyType"
    )
    interval_week: Optional[StrictInt] = Field(
        default=None,
        description="The weekly intervals at which a payment will be made. e.g. 1 = Every months, 2 = Every 2 months.",
        alias="intervalWeek",
    )
    interval_month: Optional[StrictInt] = Field(
        default=None,
        description="The monthly intervals at which a payment will be made. e.g. 1 = Every month, 2 = Every 2 months",
        alias="intervalMonth",
    )
    execution_day: Optional[StrictInt] = Field(
        default=None,
        description="The day on which a payment will be made, according to the weekly or monthly interval.",
        alias="executionDay",
    )
    __properties: ClassVar[List[str]] = [
        "frequencyType",
        "intervalWeek",
        "intervalMonth",
        "executionDay",
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
                "frequencyType": obj.get("frequencyType"),
                "intervalWeek": obj.get("intervalWeek"),
                "intervalMonth": obj.get("intervalMonth"),
                "executionDay": obj.get("executionDay"),
            }
        )
        return _obj
