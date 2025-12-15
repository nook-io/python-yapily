from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from yapily.models.amount import Amount
from typing import Optional, Set
from typing_extensions import Self


class CreateHostedVRPPaymentRequest(BaseModel):
    payment_idempotency_id: StrictStr = Field(
        description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        alias="paymentIdempotencyId",
    )
    amount: Amount
    __properties: ClassVar[List[str]] = ["paymentIdempotencyId", "amount"]
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
        if self.amount:
            _dict["amount"] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "paymentIdempotencyId": obj.get("paymentIdempotencyId"),
                "amount": Amount.from_dict(obj["amount"])
                if obj.get("amount") is not None
                else None,
            }
        )
        return _obj
