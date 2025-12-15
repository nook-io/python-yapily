from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.international_payment_request import InternationalPaymentRequest
from yapily.models.payee import Payee
from yapily.models.payer import Payer
from yapily.models.payment_context_type import PaymentContextType
from yapily.models.payment_type import PaymentType
from yapily.models.periodic_payment_request import PeriodicPaymentRequest
from typing import Set
from typing_extensions import Self


class PaymentRequest(BaseModel):
    payment_idempotency_id: StrictStr = Field(
        description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        alias="paymentIdempotencyId",
    )
    payer: Optional[Payer] = None
    reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    context_type: Optional[PaymentContextType] = Field(
        default=PaymentContextType.OTHER, alias="contextType"
    )
    purpose_code: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment purpose code. <br><br>Allowed values: INTP, DEPT, BEXP, LICF, SERV, SUPP, TRAD, SUBS, GDSV, ROYA, COMT, CHAR, ECPR, CLPR, INTE, LOAN, LOAR, INPC, INPR, INSC, INSU, LIFI, PPTI, HLRP, HLST, PDEP, IVPT, REBT, REFU, CDBL, CPKC, EDUC, FEES, GAMB, LOTT, GIFT, INSM, REOD, GOVT, TCSC, BLDM, RENT, DIVD, INVS, SAVG, HLTI, DNTS, LTCF, MDCS, VIEW, BECH, BENE, SSBE, PEFC, PENS, ADCS, BONU, COMM, SALA, ESTX, HSTX, INTX, PTXP, RDTX, TAXS, VATX, WHLD, TAXR, CBTV, ELEC, GASB, PHON, UBIL, WTER . <br><br>See [Payment Purpose code](https://docs.yapily.com/pages/payments/payments-resources/tri-pilot/) to see the definition of each code",
        alias="purposeCode",
    )
    type: PaymentType
    payee: Payee
    periodic_payment: Optional[PeriodicPaymentRequest] = Field(
        default=None, alias="periodicPayment"
    )
    international_payment: Optional[InternationalPaymentRequest] = Field(
        default=None, alias="internationalPayment"
    )
    amount: Amount
    payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Used to specify the date of the payment when the payment type is one of the following:<ul>    <li><code>DOMESTIC_SCHEDULED_PAYMENT</code></li>    <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>    <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>    <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>",
        alias="paymentDateTime",
    )
    read_refund_account: Optional[StrictBool] = Field(
        default=None,
        description="__Optional__. Used to request the payer details in the payment response when the `Institution` provides the feature `READ_DOMESTIC_SINGLE_REFUND`.<br><br>See [Reverse Payments](https://docs.yapily.com/pages/knowledge/open-banking/reverse_payments/) for more information.",
        alias="readRefundAccount",
    )
    __properties: ClassVar[List[str]] = [
        "paymentIdempotencyId",
        "payer",
        "reference",
        "contextType",
        "purposeCode",
        "type",
        "payee",
        "periodicPayment",
        "internationalPayment",
        "amount",
        "paymentDateTime",
        "readRefundAccount",
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
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        if self.periodic_payment:
            _dict["periodicPayment"] = self.periodic_payment.to_dict()
        if self.international_payment:
            _dict["internationalPayment"] = self.international_payment.to_dict()
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
                "paymentIdempotencyId": obj.get("paymentIdempotencyId"),
                "payer": Payer.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "reference": obj.get("reference"),
                "contextType": obj.get("contextType")
                if obj.get("contextType") is not None
                else PaymentContextType.OTHER,
                "purposeCode": obj.get("purposeCode"),
                "type": obj.get("type"),
                "payee": Payee.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "periodicPayment": PeriodicPaymentRequest.from_dict(
                    obj["periodicPayment"]
                )
                if obj.get("periodicPayment") is not None
                else None,
                "internationalPayment": InternationalPaymentRequest.from_dict(
                    obj["internationalPayment"]
                )
                if obj.get("internationalPayment") is not None
                else None,
                "amount": Amount.from_dict(obj["amount"])
                if obj.get("amount") is not None
                else None,
                "paymentDateTime": obj.get("paymentDateTime"),
                "readRefundAccount": obj.get("readRefundAccount"),
            }
        )
        return _obj
