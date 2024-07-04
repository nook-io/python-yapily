# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.amount import Amount
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails
from yapily.models.hosted_vrp_payer_response import HostedVrpPayerResponse
from yapily.models.hosted_vrp_refund_account import HostedVrpRefundAccount
from yapily.models.payee import Payee
from yapily.models.payment_risk import PaymentRisk

class HostedVRPPaymentResponse(BaseModel):
    """
    HostedVRPPaymentResponse
    """
    id: Optional[StrictStr] = None
    payment_idempotency_id: Optional[StrictStr] = Field(None, alias="paymentIdempotencyId")
    amount: Optional[Amount] = None
    reference: Optional[StrictStr] = Field(None, description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.")
    payee: Optional[Payee] = None
    payer: Optional[HostedVrpPayerResponse] = None
    refund_account: Optional[HostedVrpRefundAccount] = Field(None, alias="refundAccount")
    risk: Optional[PaymentRisk] = None
    payment_lifecycle_id: Optional[StrictStr] = Field(None, alias="paymentLifecycleId", description="The Unique Identifier provided by TPP in the Payment request to identify the payment.")
    expected_execution_time: Optional[datetime] = Field(None, alias="expectedExecutionTime")
    expected_settlement_time: Optional[datetime] = Field(None, alias="expectedSettlementTime")
    institution_payment_id: Optional[StrictStr] = Field(None, alias="institutionPaymentId")
    status_details: Optional[HostedPaymentStatusDetails] = Field(None, alias="statusDetails")
    __properties = ["id", "paymentIdempotencyId", "amount", "reference", "payee", "payer", "refundAccount", "risk", "paymentLifecycleId", "expectedExecutionTime", "expectedSettlementTime", "institutionPaymentId", "statusDetails"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HostedVRPPaymentResponse:
        """Create an instance of HostedVRPPaymentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict['payee'] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict['payer'] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refund_account
        if self.refund_account:
            _dict['refundAccount'] = self.refund_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of risk
        if self.risk:
            _dict['risk'] = self.risk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_details
        if self.status_details:
            _dict['statusDetails'] = self.status_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HostedVRPPaymentResponse:
        """Create an instance of HostedVRPPaymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedVRPPaymentResponse.parse_obj(obj)

        _obj = HostedVRPPaymentResponse.parse_obj({
            "id": obj.get("id"),
            "payment_idempotency_id": obj.get("paymentIdempotencyId"),
            "amount": Amount.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "reference": obj.get("reference"),
            "payee": Payee.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
            "payer": HostedVrpPayerResponse.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
            "refund_account": HostedVrpRefundAccount.from_dict(obj.get("refundAccount")) if obj.get("refundAccount") is not None else None,
            "risk": PaymentRisk.from_dict(obj.get("risk")) if obj.get("risk") is not None else None,
            "payment_lifecycle_id": obj.get("paymentLifecycleId"),
            "expected_execution_time": obj.get("expectedExecutionTime"),
            "expected_settlement_time": obj.get("expectedSettlementTime"),
            "institution_payment_id": obj.get("institutionPaymentId"),
            "status_details": HostedPaymentStatusDetails.from_dict(obj.get("statusDetails")) if obj.get("statusDetails") is not None else None
        })
        return _obj


