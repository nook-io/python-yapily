from __future__ import annotations
import pprint
import json
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self


class EnrichedPredictedBalance(BaseModel):
    var_date: Optional[date] = Field(
        default=None,
        description="The date for which Balance amount is predicted.",
        alias="date",
    )
    median_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The median Balance amount for a future date.",
        alias="medianBalance",
    )
    var_90percentile_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The 90th percentile Balance amount for a future date.",
        alias="90percentileBalance",
    )
    var_10percentile_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The 10th percentile Balance amount for a future date.",
        alias="10percentileBalance",
    )
    __properties: ClassVar[List[str]] = [
        "date",
        "medianBalance",
        "90percentileBalance",
        "10percentileBalance",
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
                "date": obj.get("date"),
                "medianBalance": obj.get("medianBalance"),
                "90percentileBalance": obj.get("90percentileBalance"),
                "10percentileBalance": obj.get("10percentileBalance"),
            }
        )
        return _obj
