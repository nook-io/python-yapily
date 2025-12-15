from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.initiation_details import InitiationDetails
from yapily.models.payer import Payer
from yapily.models.payment_status import PaymentStatus
from yapily.models.payment_status_details import PaymentStatusDetails
from yapily.models.refund_account import RefundAccount
from yapily.models.submission_details import SubmissionDetails
from typing import Set
from typing_extensions import Self


class SubmissionResponse(BaseModel):
    id: Optional[StrictStr] = None
    payment_idempotency_id: Optional[StrictStr] = Field(
        default=None, alias="paymentIdempotencyId"
    )
    payment_lifecycle_id: Optional[StrictStr] = Field(
        default=None, alias="paymentLifecycleId"
    )
    institution_consent_id: Optional[StrictStr] = Field(
        default=None, alias="institutionConsentId"
    )
    status: Optional[PaymentStatus] = None
    status_details: Optional[PaymentStatusDetails] = Field(
        default=None, alias="statusDetails"
    )
    initiation_details: InitiationDetails = Field(alias="initiationDetails")
    submission_details: SubmissionDetails = Field(alias="submissionDetails")
    payer: Optional[Payer] = None
    refund_account: Optional[RefundAccount] = Field(default=None, alias="refundAccount")
    expected_execution_time: Optional[datetime] = Field(
        default=None, alias="expectedExecutionTime"
    )
    expected_settlement_time: Optional[datetime] = Field(
        default=None, alias="expectedSettlementTime"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "paymentIdempotencyId",
        "paymentLifecycleId",
        "institutionConsentId",
        "status",
        "statusDetails",
        "initiationDetails",
        "submissionDetails",
        "payer",
        "refundAccount",
        "expectedExecutionTime",
        "expectedSettlementTime",
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
        if self.initiation_details:
            _dict["initiationDetails"] = self.initiation_details.to_dict()
        if self.submission_details:
            _dict["submissionDetails"] = self.submission_details.to_dict()
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.refund_account:
            _dict["refundAccount"] = self.refund_account.to_dict()
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
                "paymentLifecycleId": obj.get("paymentLifecycleId"),
                "institutionConsentId": obj.get("institutionConsentId"),
                "status": obj.get("status"),
                "statusDetails": PaymentStatusDetails.from_dict(obj["statusDetails"])
                if obj.get("statusDetails") is not None
                else None,
                "initiationDetails": InitiationDetails.from_dict(
                    obj["initiationDetails"]
                )
                if obj.get("initiationDetails") is not None
                else None,
                "submissionDetails": SubmissionDetails.from_dict(
                    obj["submissionDetails"]
                )
                if obj.get("submissionDetails") is not None
                else None,
                "payer": Payer.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "refundAccount": RefundAccount.from_dict(obj["refundAccount"])
                if obj.get("refundAccount") is not None
                else None,
                "expectedExecutionTime": obj.get("expectedExecutionTime"),
                "expectedSettlementTime": obj.get("expectedSettlementTime"),
            }
        )
        return _obj
