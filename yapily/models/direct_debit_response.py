from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.direct_debit_payee import DirectDebitPayee
from yapily.models.payment_status_details import PaymentStatusDetails
from typing import Set
from typing_extensions import Self


class DirectDebitResponse(BaseModel):
    id: Optional[StrictStr] = None
    status_details: Optional[PaymentStatusDetails] = Field(
        default=None, alias="statusDetails"
    )
    payee_details: Optional[DirectDebitPayee] = Field(
        default=None, alias="payeeDetails"
    )
    reference: Optional[StrictStr] = None
    previous_payment_amount: Optional[Amount] = Field(
        default=None, alias="previousPaymentAmount"
    )
    previous_payment_date_time: Optional[datetime] = Field(
        default=None, alias="previousPaymentDateTime"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "statusDetails",
        "payeeDetails",
        "reference",
        "previousPaymentAmount",
        "previousPaymentDateTime",
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
        if self.status_details:
            _dict["statusDetails"] = self.status_details.to_dict()
        if self.payee_details:
            _dict["payeeDetails"] = self.payee_details.to_dict()
        if self.previous_payment_amount:
            _dict["previousPaymentAmount"] = self.previous_payment_amount.to_dict()
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
                "statusDetails": PaymentStatusDetails.from_dict(obj["statusDetails"])
                if obj.get("statusDetails") is not None
                else None,
                "payeeDetails": DirectDebitPayee.from_dict(obj["payeeDetails"])
                if obj.get("payeeDetails") is not None
                else None,
                "reference": obj.get("reference"),
                "previousPaymentAmount": Amount.from_dict(obj["previousPaymentAmount"])
                if obj.get("previousPaymentAmount") is not None
                else None,
                "previousPaymentDateTime": obj.get("previousPaymentDateTime"),
            }
        )
        return _obj
