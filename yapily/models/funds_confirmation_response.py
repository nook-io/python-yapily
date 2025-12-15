from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.funds_available import FundsAvailable
from typing import Set
from typing_extensions import Self


class FundsConfirmationResponse(BaseModel):
    id: Optional[StrictStr] = None
    reference: Optional[StrictStr] = Field(
        default=None,
        description="The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    payment_amount: Amount = Field(alias="paymentAmount")
    funds_available: FundsAvailable = Field(alias="fundsAvailable")
    __properties: ClassVar[List[str]] = [
        "id",
        "reference",
        "paymentAmount",
        "fundsAvailable",
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
        if self.funds_available:
            _dict["fundsAvailable"] = self.funds_available.to_dict()
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
                "reference": obj.get("reference"),
                "paymentAmount": Amount.from_dict(obj["paymentAmount"])
                if obj.get("paymentAmount") is not None
                else None,
                "fundsAvailable": FundsAvailable.from_dict(obj["fundsAvailable"])
                if obj.get("fundsAvailable") is not None
                else None,
            }
        )
        return _obj
