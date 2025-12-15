from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.hosted_payment_phase import HostedPaymentPhase
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails
from yapily.models.institution_identifiers_response import (
    InstitutionIdentifiersResponse,
)
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_type_response import PaymentTypeResponse
from typing import Set
from typing_extensions import Self


class HostedPayment(BaseModel):
    payment_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier of the payment.",
        alias="paymentId",
    )
    hosted_payment_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier of the payment created using Yapily hosted application.",
        alias="hostedPaymentId",
    )
    consent_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier of the consent.",
        alias="consentId",
    )
    institution_identifiers: Optional[InstitutionIdentifiersResponse] = Field(
        default=None, alias="institutionIdentifiers"
    )
    phases: Optional[List[HostedPaymentPhase]] = Field(
        default=None, description="The phase reached by the payment and its timestamp."
    )
    payment_status: Optional[StrictStr] = Field(
        default=None,
        description="Payment status based on latest HostedAuthPaymentPhase in phases. Value can be <ul> <li>PENDING  -  Payment pending processing</li> <li>COMPLETED  -  Payment processing completed</li> <li>FAILED  -  Payment process failed</li></ul>",
        alias="paymentStatus",
    )
    status_details: Optional[List[HostedPaymentStatusDetails]] = Field(
        default=None,
        description="Details of the payment status.",
        alias="statusDetails",
    )
    institution_payment_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier of the payment created with the `Institution`.",
        alias="institutionPaymentId",
    )
    payment_lifecycle_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier provided by TPP in the Payment request to identify the payment.",
        alias="paymentLifecycleId",
    )
    payment_idempotency_id: Optional[StrictStr] = Field(
        default=None,
        description="A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        alias="paymentIdempotencyId",
    )
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
    amount: Optional[AmountDetailsResponse] = None
    __properties: ClassVar[List[str]] = [
        "paymentId",
        "hostedPaymentId",
        "consentId",
        "institutionIdentifiers",
        "phases",
        "paymentStatus",
        "statusDetails",
        "institutionPaymentId",
        "paymentLifecycleId",
        "paymentIdempotencyId",
        "reference",
        "contextType",
        "type",
        "payee",
        "payer",
        "amount",
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
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        _items = []
        if self.phases:
            for _item_phases in self.phases:
                if _item_phases:
                    _items.append(_item_phases.to_dict())
            _dict["phases"] = _items
        _items = []
        if self.status_details:
            for _item_status_details in self.status_details:
                if _item_status_details:
                    _items.append(_item_status_details.to_dict())
            _dict["statusDetails"] = _items
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
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
                "paymentId": obj.get("paymentId"),
                "hostedPaymentId": obj.get("hostedPaymentId"),
                "consentId": obj.get("consentId"),
                "institutionIdentifiers": InstitutionIdentifiersResponse.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "phases": [
                    HostedPaymentPhase.from_dict(_item) for _item in obj["phases"]
                ]
                if obj.get("phases") is not None
                else None,
                "paymentStatus": obj.get("paymentStatus"),
                "statusDetails": [
                    HostedPaymentStatusDetails.from_dict(_item)
                    for _item in obj["statusDetails"]
                ]
                if obj.get("statusDetails") is not None
                else None,
                "institutionPaymentId": obj.get("institutionPaymentId"),
                "paymentLifecycleId": obj.get("paymentLifecycleId"),
                "paymentIdempotencyId": obj.get("paymentIdempotencyId"),
                "reference": obj.get("reference"),
                "contextType": obj.get("contextType"),
                "type": obj.get("type"),
                "payee": PayeeDetailsResponse.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "payer": PayerDetailsResponse.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "amount": AmountDetailsResponse.from_dict(obj["amount"])
                if obj.get("amount") is not None
                else None,
            }
        )
        return _obj
