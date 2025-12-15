from __future__ import annotations
import pprint
import json
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_type_response import PaymentTypeResponse
from typing import Set
from typing_extensions import Self


class HostedPaymentRequestDetailsLink(BaseModel):
    reference: Optional[StrictStr] = Field(
        default=None,
        description="The payment reference or description. Limited to a maximum of 18 characters for UK institutions.",
    )
    context_type: Optional[PaymentContextTypeResponse] = Field(
        default=None, alias="contextType"
    )
    type: Optional[PaymentTypeResponse] = None
    payee: Optional[PayeeDetailsResponse] = None
    payer: Optional[PayerDetailsResponse] = None
    amount_details: Optional[AmountDetailsResponse] = Field(
        default=None, alias="amountDetails"
    )
    payment_due_date: Optional[date] = Field(
        default=None,
        description="The date that the payment is due. Displayed to the end user in the payment summary screen.",
        alias="paymentDueDate",
    )
    __properties: ClassVar[List[str]] = [
        "reference",
        "contextType",
        "type",
        "payee",
        "payer",
        "amountDetails",
        "paymentDueDate",
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
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.amount_details:
            _dict["amountDetails"] = self.amount_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "reference": obj.get("reference"),
                "contextType": obj.get("contextType"),
                "type": obj.get("type"),
                "payee": PayeeDetailsResponse.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "payer": PayerDetailsResponse.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "amountDetails": AmountDetailsResponse.from_dict(obj["amountDetails"])
                if obj.get("amountDetails") is not None
                else None,
                "paymentDueDate": obj.get("paymentDueDate"),
            }
        )
        return _obj
