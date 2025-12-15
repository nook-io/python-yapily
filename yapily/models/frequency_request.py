from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.frequency_enum_extended import FrequencyEnumExtended
from typing import Set
from typing_extensions import Self


class FrequencyRequest(BaseModel):
    type: FrequencyEnumExtended
    interval_week: Optional[StrictInt] = Field(
        default=None,
        description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        alias="intervalWeek",
    )
    interval_month: Optional[StrictInt] = Field(
        default=None,
        description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        alias="intervalMonth",
    )
    execution_day: Optional[StrictInt] = Field(
        default=None,
        description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        alias="executionDay",
    )
    __properties: ClassVar[List[str]] = [
        "type",
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
                "type": obj.get("type"),
                "intervalWeek": obj.get("intervalWeek"),
                "intervalMonth": obj.get("intervalMonth"),
                "executionDay": obj.get("executionDay"),
            }
        )
        return _obj
