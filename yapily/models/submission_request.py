from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.payment_context_type import PaymentContextType
from typing import Set
from typing_extensions import Self


class SubmissionRequest(BaseModel):
    payment_idempotency_id: StrictStr = Field(
        description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        alias="paymentIdempotencyId",
    )
    psu_authentication_method: StrictStr = Field(
        description="__Mandatory__. Chosen authentication method for submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED].",
        alias="psuAuthenticationMethod",
    )
    context_type: Optional[PaymentContextType] = Field(
        default=PaymentContextType.OTHER, alias="contextType"
    )
    payment_amount: Amount = Field(alias="paymentAmount")
    __properties: ClassVar[List[str]] = [
        "paymentIdempotencyId",
        "psuAuthenticationMethod",
        "contextType",
        "paymentAmount",
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
        if self.payment_amount:
            _dict["paymentAmount"] = self.payment_amount.to_dict()
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
                "psuAuthenticationMethod": obj.get("psuAuthenticationMethod"),
                "contextType": obj.get("contextType")
                if obj.get("contextType") is not None
                else PaymentContextType.OTHER,
                "paymentAmount": Amount.from_dict(obj["paymentAmount"])
                if obj.get("paymentAmount") is not None
                else None,
            }
        )
        return _obj
