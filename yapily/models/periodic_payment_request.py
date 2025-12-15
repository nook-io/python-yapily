from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.frequency_request import FrequencyRequest
from typing import Set
from typing_extensions import Self


class PeriodicPaymentRequest(BaseModel):
    frequency: FrequencyRequest
    number_of_payments: Optional[StrictInt] = Field(
        default=None,
        description="__Conditional__. Defines the total number of payments to be made.<br><br>This is required if `finalPaymentDateTime` is not specified and it is intended for the periodic payment have a fixed amount of payments.",
        alias="numberOfPayments",
    )
    next_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Defines when to start the recurring payment date and time. Specify this if you want the first payment to start on a different day than what the frequency object defines.",
        alias="nextPaymentDateTime",
    )
    next_payment_amount: Optional[Amount] = Field(
        default=None, alias="nextPaymentAmount"
    )
    final_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Defines the final payment date and time. To create an open-ended periodic payment, do not specify this property.",
        alias="finalPaymentDateTime",
    )
    final_payment_amount: Optional[Amount] = Field(
        default=None, alias="finalPaymentAmount"
    )
    __properties: ClassVar[List[str]] = [
        "frequency",
        "numberOfPayments",
        "nextPaymentDateTime",
        "nextPaymentAmount",
        "finalPaymentDateTime",
        "finalPaymentAmount",
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
        if self.frequency:
            _dict["frequency"] = self.frequency.to_dict()
        if self.next_payment_amount:
            _dict["nextPaymentAmount"] = self.next_payment_amount.to_dict()
        if self.final_payment_amount:
            _dict["finalPaymentAmount"] = self.final_payment_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "frequency": FrequencyRequest.from_dict(obj["frequency"])
                if obj.get("frequency") is not None
                else None,
                "numberOfPayments": obj.get("numberOfPayments"),
                "nextPaymentDateTime": obj.get("nextPaymentDateTime"),
                "nextPaymentAmount": Amount.from_dict(obj["nextPaymentAmount"])
                if obj.get("nextPaymentAmount") is not None
                else None,
                "finalPaymentDateTime": obj.get("finalPaymentDateTime"),
                "finalPaymentAmount": Amount.from_dict(obj["finalPaymentAmount"])
                if obj.get("finalPaymentAmount") is not None
                else None,
            }
        )
        return _obj
