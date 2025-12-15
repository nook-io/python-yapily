from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from yapily.models.amount import Amount
from yapily.models.exchange_rate_information_response import (
    ExchangeRateInformationResponse,
)
from yapily.models.frequency_response import FrequencyResponse
from yapily.models.payee import Payee
from yapily.models.payer import Payer
from yapily.models.payment_charge_details import PaymentChargeDetails
from yapily.models.payment_status import PaymentStatus
from yapily.models.payment_status_details import PaymentStatusDetails
from yapily.models.priority_code_enum import PriorityCodeEnum
from yapily.models.refund_account import RefundAccount
from typing import Set
from typing_extensions import Self


class PaymentResponse(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the payment."
    )
    institution_consent_id: Optional[StrictStr] = Field(
        default=None,
        description="Identification of the consent at the Institution.",
        alias="institutionConsentId",
    )
    payment_idempotency_id: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        alias="paymentIdempotencyId",
    )
    payment_lifecycle_id: Optional[StrictStr] = Field(
        default=None, alias="paymentLifecycleId"
    )
    status: Optional[PaymentStatus] = None
    status_details: Optional[PaymentStatusDetails] = Field(
        default=None, alias="statusDetails"
    )
    payer: Optional[Payer] = None
    payee_details: Optional[Payee] = Field(default=None, alias="payeeDetails")
    reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Monetary amount."
    )
    currency: Optional[StrictStr] = Field(
        default=None,
        description="Currency the payment amount is denoted in. Specified as a 3-letter ISO 4217 code.",
    )
    amount_details: Optional[Amount] = Field(default=None, alias="amountDetails")
    created_at: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the payment request was created.",
        alias="createdAt",
    )
    first_payment_amount: Optional[Amount] = Field(
        default=None, alias="firstPaymentAmount"
    )
    first_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the first payment request is to be made.",
        alias="firstPaymentDateTime",
    )
    next_payment_amount: Optional[Amount] = Field(
        default=None, alias="nextPaymentAmount"
    )
    next_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Defines when the recurring payment is to be made.",
        alias="nextPaymentDateTime",
    )
    final_payment_amount: Optional[Amount] = Field(
        default=None, alias="finalPaymentAmount"
    )
    final_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the final payment is to be made.",
        alias="finalPaymentDateTime",
    )
    number_of_payments: Optional[StrictInt] = Field(
        default=None,
        description="Number of recurring payment requests to be made as part of the instructed payment schedule.",
        alias="numberOfPayments",
    )
    previous_payment_amount: Optional[Amount] = Field(
        default=None, alias="previousPaymentAmount"
    )
    previous_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the previous payment request was posted.",
        alias="previousPaymentDateTime",
    )
    charge_details: Optional[List[PaymentChargeDetails]] = Field(
        default=None, alias="chargeDetails"
    )
    scheduled_payment_type: Optional[StrictStr] = Field(
        default=None,
        description="Details the execution type and the payment date between the payer and the payee.",
        alias="scheduledPaymentType",
    )
    scheduled_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the scheduled payment request will be made.",
        alias="scheduledPaymentDateTime",
    )
    frequency: Optional[FrequencyResponse] = None
    currency_of_transfer: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. The currency to be transferred to the payee. This may differ from the currency the payment is denoted in and the currency of the payer's account. Specified as a 3-letter code (ISO 4217).",
        alias="currencyOfTransfer",
    )
    purpose: Optional[StrictStr] = Field(
        default=None,
        description="Specifies the external purpose code for the `Institution` - IS0 20022.",
    )
    priority: Optional[PriorityCodeEnum] = None
    exchange_rate: Optional[ExchangeRateInformationResponse] = Field(
        default=None, alias="exchangeRate"
    )
    refund_account: Optional[RefundAccount] = Field(default=None, alias="refundAccount")
    bulk_amount_sum: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="bulkAmountSum"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "institutionConsentId",
        "paymentIdempotencyId",
        "paymentLifecycleId",
        "status",
        "statusDetails",
        "payer",
        "payeeDetails",
        "reference",
        "amount",
        "currency",
        "amountDetails",
        "createdAt",
        "firstPaymentAmount",
        "firstPaymentDateTime",
        "nextPaymentAmount",
        "nextPaymentDateTime",
        "finalPaymentAmount",
        "finalPaymentDateTime",
        "numberOfPayments",
        "previousPaymentAmount",
        "previousPaymentDateTime",
        "chargeDetails",
        "scheduledPaymentType",
        "scheduledPaymentDateTime",
        "frequency",
        "currencyOfTransfer",
        "purpose",
        "priority",
        "exchangeRate",
        "refundAccount",
        "bulkAmountSum",
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
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.payee_details:
            _dict["payeeDetails"] = self.payee_details.to_dict()
        if self.amount_details:
            _dict["amountDetails"] = self.amount_details.to_dict()
        if self.first_payment_amount:
            _dict["firstPaymentAmount"] = self.first_payment_amount.to_dict()
        if self.next_payment_amount:
            _dict["nextPaymentAmount"] = self.next_payment_amount.to_dict()
        if self.final_payment_amount:
            _dict["finalPaymentAmount"] = self.final_payment_amount.to_dict()
        if self.previous_payment_amount:
            _dict["previousPaymentAmount"] = self.previous_payment_amount.to_dict()
        _items = []
        if self.charge_details:
            for _item_charge_details in self.charge_details:
                if _item_charge_details:
                    _items.append(_item_charge_details.to_dict())
            _dict["chargeDetails"] = _items
        if self.frequency:
            _dict["frequency"] = self.frequency.to_dict()
        if self.exchange_rate:
            _dict["exchangeRate"] = self.exchange_rate.to_dict()
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
                "institutionConsentId": obj.get("institutionConsentId"),
                "paymentIdempotencyId": obj.get("paymentIdempotencyId"),
                "paymentLifecycleId": obj.get("paymentLifecycleId"),
                "status": obj.get("status"),
                "statusDetails": PaymentStatusDetails.from_dict(obj["statusDetails"])
                if obj.get("statusDetails") is not None
                else None,
                "payer": Payer.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "payeeDetails": Payee.from_dict(obj["payeeDetails"])
                if obj.get("payeeDetails") is not None
                else None,
                "reference": obj.get("reference"),
                "amount": obj.get("amount"),
                "currency": obj.get("currency"),
                "amountDetails": Amount.from_dict(obj["amountDetails"])
                if obj.get("amountDetails") is not None
                else None,
                "createdAt": obj.get("createdAt"),
                "firstPaymentAmount": Amount.from_dict(obj["firstPaymentAmount"])
                if obj.get("firstPaymentAmount") is not None
                else None,
                "firstPaymentDateTime": obj.get("firstPaymentDateTime"),
                "nextPaymentAmount": Amount.from_dict(obj["nextPaymentAmount"])
                if obj.get("nextPaymentAmount") is not None
                else None,
                "nextPaymentDateTime": obj.get("nextPaymentDateTime"),
                "finalPaymentAmount": Amount.from_dict(obj["finalPaymentAmount"])
                if obj.get("finalPaymentAmount") is not None
                else None,
                "finalPaymentDateTime": obj.get("finalPaymentDateTime"),
                "numberOfPayments": obj.get("numberOfPayments"),
                "previousPaymentAmount": Amount.from_dict(obj["previousPaymentAmount"])
                if obj.get("previousPaymentAmount") is not None
                else None,
                "previousPaymentDateTime": obj.get("previousPaymentDateTime"),
                "chargeDetails": [
                    PaymentChargeDetails.from_dict(_item)
                    for _item in obj["chargeDetails"]
                ]
                if obj.get("chargeDetails") is not None
                else None,
                "scheduledPaymentType": obj.get("scheduledPaymentType"),
                "scheduledPaymentDateTime": obj.get("scheduledPaymentDateTime"),
                "frequency": FrequencyResponse.from_dict(obj["frequency"])
                if obj.get("frequency") is not None
                else None,
                "currencyOfTransfer": obj.get("currencyOfTransfer"),
                "purpose": obj.get("purpose"),
                "priority": obj.get("priority"),
                "exchangeRate": ExchangeRateInformationResponse.from_dict(
                    obj["exchangeRate"]
                )
                if obj.get("exchangeRate") is not None
                else None,
                "refundAccount": RefundAccount.from_dict(obj["refundAccount"])
                if obj.get("refundAccount") is not None
                else None,
                "bulkAmountSum": obj.get("bulkAmountSum"),
            }
        )
        return _obj
