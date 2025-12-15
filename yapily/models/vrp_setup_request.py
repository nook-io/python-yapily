from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.hosted_vrp_limits_request import HostedVRPLimitsRequest
from yapily.models.payee import Payee
from yapily.models.payer import Payer
from yapily.models.payment_risk import PaymentRisk
from typing import Set
from typing_extensions import Self


class VRPSetupRequest(BaseModel):
    payer: Optional[Payer] = None
    payee: Payee
    reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    limits: Optional[HostedVRPLimitsRequest] = None
    valid_from: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Start date when the consent becomes valid.",
        alias="validFrom",
    )
    valid_to: Optional[datetime] = Field(
        default=None,
        description="__Optional__. End date when the consent expires and becomes invalid.",
        alias="validTo",
    )
    recurring_payment_category: Optional[StrictStr] = Field(
        default=None,
        description="The use-case for the VRP consent supported by the bank. Allowed values: <br>`ONGOING` <br>`SUBSCRIPTION`",
        alias="recurringPaymentCategory",
    )
    initial_payment: Optional[Amount] = Field(
        default=None,
        description="__Optional__. Initial payment to be charged under this consent. If enforced, this amount must match the first payment amount executed using this consent.",
        alias="initialPayment",
    )
    risk: Optional[PaymentRisk] = None
    __properties: ClassVar[List[str]] = [
        "payer",
        "payee",
        "reference",
        "limits",
        "validFrom",
        "validTo",
        "recurringPaymentCategory",
        "initialPayment",
        "risk",
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
        if self.limits:
            _dict["limits"] = self.limits.to_dict()
        if self.initial_payment:
            _dict["initialPayment"] = self.initial_payment.to_dict()
        if self.risk:
            _dict["risk"] = self.risk.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "payer": Payer.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "payee": Payee.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "reference": obj.get("reference"),
                "limits": HostedVRPLimitsRequest.from_dict(obj["limits"])
                if obj.get("limits") is not None
                else None,
                "validFrom": obj.get("validFrom"),
                "validTo": obj.get("validTo"),
                "recurringPaymentCategory": obj.get("recurringPaymentCategory"),
                "initialPayment": Amount.from_dict(obj["initialPayment"])
                if obj.get("initialPayment") is not None
                else None,
                "risk": PaymentRisk.from_dict(obj["risk"])
                if obj.get("risk") is not None
                else None,
            }
        )
        return _obj
