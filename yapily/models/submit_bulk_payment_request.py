from __future__ import annotations
import pprint
import re
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from yapily.models.payment_request import PaymentRequest
from typing import Set
from typing_extensions import Self


class SubmitBulkPaymentRequest(BaseModel):
    idempotency_id: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=40)]
    ] = Field(
        default=None,
        description="__Optional__. An alphanumeric string (1-40 chars) used for idempotency. Unique per consent ID for 24 hours. Prevents duplicate bulk file payment submissions.",
        alias="idempotencyId",
    )
    payments: List[PaymentRequest] = Field(
        description="__Mandatory__. The array of `PaymentRequest` objects to initiate in the bulk payment."
    )
    originator_identification_number: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. The identification number of the originator.<ul><li>Mandatory for AIB bulk payments</li></ul>",
        alias="originatorIdentificationNumber",
    )
    execution_date_time: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Used to schedule the bulk payment to be executed at a future date if supported by the `Institution`.",
        alias="executionDateTime",
    )
    __properties: ClassVar[List[str]] = [
        "idempotencyId",
        "payments",
        "originatorIdentificationNumber",
        "executionDateTime",
    ]

    @field_validator("idempotency_id")
    def idempotency_id_validate_regular_expression(cls, value):
        if value is None:
            return value
        if not re.match(r"^\S{1,40}$", value):
            raise ValueError(r"must validate the regular expression /^\S{1,40}$/")
        return value

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
        _items = []
        if self.payments:
            for _item_payments in self.payments:
                if _item_payments:
                    _items.append(_item_payments.to_dict())
            _dict["payments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "idempotencyId": obj.get("idempotencyId"),
                "payments": [
                    PaymentRequest.from_dict(_item) for _item in obj["payments"]
                ]
                if obj.get("payments") is not None
                else None,
                "originatorIdentificationNumber": obj.get(
                    "originatorIdentificationNumber"
                ),
                "executionDateTime": obj.get("executionDateTime"),
            }
        )
        return _obj
