from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.charge_bearer_type import ChargeBearerType
from yapily.models.exchange_rate_information import ExchangeRateInformation
from yapily.models.priority_code_enum import PriorityCodeEnum
from typing import Set
from typing_extensions import Self


class InternationalPaymentRequest(BaseModel):
    currency_of_transfer: StrictStr = Field(
        description="__Mandatory__. The currency to be transferred to the payee. This may differ from the currency the payment is denoted in and the currency of the payer's account. Specified as a 3-letter code (ISO 4217).",
        alias="currencyOfTransfer",
    )
    exchange_rate_information: Optional[ExchangeRateInformation] = Field(
        default=None, alias="exchangeRateInformation"
    )
    purpose: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. Used to indicate the external purpose as a [ISO20022 purpose code](https://www.rba.hr/documents/20182/183267/External+purpose+codes+list/8a28f888-1f83-5e29-d6ed-fce05f428689?version=1.1) value.",
    )
    priority: Optional[PriorityCodeEnum] = None
    charge_bearer: Optional[ChargeBearerType] = Field(
        default=None, alias="chargeBearer"
    )
    __properties: ClassVar[List[str]] = [
        "currencyOfTransfer",
        "exchangeRateInformation",
        "purpose",
        "priority",
        "chargeBearer",
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
        if self.exchange_rate_information:
            _dict["exchangeRateInformation"] = self.exchange_rate_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "currencyOfTransfer": obj.get("currencyOfTransfer"),
                "exchangeRateInformation": ExchangeRateInformation.from_dict(
                    obj["exchangeRateInformation"]
                )
                if obj.get("exchangeRateInformation") is not None
                else None,
                "purpose": obj.get("purpose"),
                "priority": obj.get("priority"),
                "chargeBearer": obj.get("chargeBearer"),
            }
        )
        return _obj
