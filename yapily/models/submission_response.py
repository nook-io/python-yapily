import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.initiation_details import InitiationDetails
from yapily.models.payer import Payer
from yapily.models.payment_status import PaymentStatus
from yapily.models.payment_status_details import PaymentStatusDetails
from yapily.models.refund_account import RefundAccount
from yapily.models.submission_details import SubmissionDetails


class SubmissionResponse(BaseModel):
    """
    SubmissionResponse
    """

    id: StrictStr | None = None
    payment_idempotency_id: Annotated[StrictStr | None, Field(alias="paymentIdempotencyId")] = None
    payment_lifecycle_id: Annotated[StrictStr | None, Field(alias="paymentLifecycleId")] = None
    institution_consent_id: Annotated[StrictStr | None, Field(alias="institutionConsentId")] = None
    status: PaymentStatus | None = None
    status_details: Annotated[PaymentStatusDetails | None, Field(alias="statusDetails")] = None
    initiation_details: Annotated[InitiationDetails, Field(alias="initiationDetails")]
    submission_details: Annotated[SubmissionDetails, Field(alias="submissionDetails")]
    payer: Payer | None = None
    refund_account: Annotated[RefundAccount | None, Field(alias="refundAccount")] = None
    expected_execution_time: Annotated[datetime | None, Field(alias="expectedExecutionTime")] = None
    expected_settlement_time: Annotated[datetime | None, Field(alias="expectedSettlementTime")] = None
    __properties = [
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
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SubmissionResponse":
        """Create an instance of SubmissionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status_details
        if self.status_details:
            _dict["statusDetails"] = self.status_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initiation_details
        if self.initiation_details:
            _dict["initiationDetails"] = self.initiation_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of submission_details
        if self.submission_details:
            _dict["submissionDetails"] = self.submission_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refund_account
        if self.refund_account:
            _dict["refundAccount"] = self.refund_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SubmissionResponse":
        """Create an instance of SubmissionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubmissionResponse.parse_obj(obj)

        return SubmissionResponse.parse_obj(
            {
                "id": obj.get("id"),
                "payment_idempotency_id": obj.get("paymentIdempotencyId"),
                "payment_lifecycle_id": obj.get("paymentLifecycleId"),
                "institution_consent_id": obj.get("institutionConsentId"),
                "status": obj.get("status"),
                "status_details": PaymentStatusDetails.from_dict(obj.get("statusDetails"))
                if obj.get("statusDetails") is not None
                else None,
                "initiation_details": InitiationDetails.from_dict(obj.get("initiationDetails"))
                if obj.get("initiationDetails") is not None
                else None,
                "submission_details": SubmissionDetails.from_dict(obj.get("submissionDetails"))
                if obj.get("submissionDetails") is not None
                else None,
                "payer": Payer.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
                "refund_account": RefundAccount.from_dict(obj.get("refundAccount"))
                if obj.get("refundAccount") is not None
                else None,
                "expected_execution_time": obj.get("expectedExecutionTime"),
                "expected_settlement_time": obj.get("expectedSettlementTime"),
            }
        )
