from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from yapily.models.amount import Amount
from typing import Optional, Set
from typing_extensions import Self


class SweepingPeriodicLimits(BaseModel):
    total_max_amount: Amount = Field(
        description="__Mandatory__. Maximum amount that can be specified in all payment instructions in a given period under this VRP consent. If the Alignment is Calendar, the limit is pro-rated in the first period to the remaining number of days.",
        alias="totalMaxAmount",
    )
    frequency: StrictStr = Field(
        description="__Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [DAILY, WEEKLY, EVERY_TWO_WEEKS, MONTHLY, YEARLY]."
    )
    alignment: StrictStr = Field(
        description="__Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question."
    )
    __properties: ClassVar[List[str]] = ["totalMaxAmount", "frequency", "alignment"]
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
        if self.total_max_amount:
            _dict["totalMaxAmount"] = self.total_max_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "totalMaxAmount": Amount.from_dict(obj["totalMaxAmount"])
                if obj.get("totalMaxAmount") is not None
                else None,
                "frequency": obj.get("frequency"),
                "alignment": obj.get("alignment"),
            }
        )
        return _obj
