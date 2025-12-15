from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails
from yapily.models.hosted_vrp_payer_response import HostedVrpPayerResponse
from yapily.models.hosted_vrp_refund_account import HostedVrpRefundAccount
from yapily.models.payee import Payee
from yapily.models.payment_risk import PaymentRisk
from typing import Set
from typing_extensions import Self


class HostedVRPPaymentResponse(BaseModel):
    id: Optional[StrictStr] = None
    payment_idempotency_id: Optional[StrictStr] = Field(
        default=None, alias="paymentIdempotencyId"
    )
    amount: Optional[Amount] = None
    reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    payee: Optional[Payee] = None
    payer: Optional[HostedVrpPayerResponse] = None
    refund_account: Optional[HostedVrpRefundAccount] = Field(
        default=None, alias="refundAccount"
    )
    risk: Optional[PaymentRisk] = None
    payment_lifecycle_id: Optional[StrictStr] = Field(
        default=None,
        description="The Unique Identifier provided by TPP in the Payment request to identify the payment.",
        alias="paymentLifecycleId",
    )
    expected_execution_time: Optional[datetime] = Field(
        default=None, alias="expectedExecutionTime"
    )
    expected_settlement_time: Optional[datetime] = Field(
        default=None, alias="expectedSettlementTime"
    )
    institution_payment_id: Optional[StrictStr] = Field(
        default=None, alias="institutionPaymentId"
    )
    status_details: Optional[HostedPaymentStatusDetails] = Field(
        default=None, alias="statusDetails"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "paymentIdempotencyId",
        "amount",
        "reference",
        "payee",
        "payer",
        "refundAccount",
        "risk",
        "paymentLifecycleId",
        "expectedExecutionTime",
        "expectedSettlementTime",
        "institutionPaymentId",
        "statusDetails",
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
        if self.amount:
            _dict["amount"] = self.amount.to_dict()
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.refund_account:
            _dict["refundAccount"] = self.refund_account.to_dict()
        if self.risk:
            _dict["risk"] = self.risk.to_dict()
        if self.status_details:
            _dict["statusDetails"] = self.status_details.to_dict()
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
                "paymentIdempotencyId": obj.get("paymentIdempotencyId"),
                "amount": Amount.from_dict(obj["amount"])
                if obj.get("amount") is not None
                else None,
                "reference": obj.get("reference"),
                "payee": Payee.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "payer": HostedVrpPayerResponse.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "refundAccount": HostedVrpRefundAccount.from_dict(obj["refundAccount"])
                if obj.get("refundAccount") is not None
                else None,
                "risk": PaymentRisk.from_dict(obj["risk"])
                if obj.get("risk") is not None
                else None,
                "paymentLifecycleId": obj.get("paymentLifecycleId"),
                "expectedExecutionTime": obj.get("expectedExecutionTime"),
                "expectedSettlementTime": obj.get("expectedSettlementTime"),
                "institutionPaymentId": obj.get("institutionPaymentId"),
                "statusDetails": HostedPaymentStatusDetails.from_dict(
                    obj["statusDetails"]
                )
                if obj.get("statusDetails") is not None
                else None,
            }
        )
        return _obj
