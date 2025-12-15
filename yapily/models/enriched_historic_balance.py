from __future__ import annotations
import pprint
import json
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self


class EnrichedHistoricBalance(BaseModel):
    var_date: Optional[date] = Field(
        default=None,
        description="The date for which Aggregated Balance amount across Bank accounts is calculated.",
        alias="date",
    )
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="The Aggregated Balance amount for a specific date."
    )
    __properties: ClassVar[List[str]] = ["date", "balance"]
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
            {"date": obj.get("date"), "balance": obj.get("balance")}
        )
        return _obj
