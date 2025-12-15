from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from yapily.models.amount import Amount
from yapily.models.vrp_periodic_limit import VrpPeriodicLimit
from typing import Set
from typing_extensions import Self


class VrpConfiguration(BaseModel):
    maximum_individual_amount: Optional[Amount] = Field(
        default=None,
        description="Maximum amount per transaction",
        alias="maximumIndividualAmount",
    )
    maximum_cumulative_amount: Optional[Amount] = Field(
        default=None,
        description="Maximum cumulative amount",
        alias="maximumCumulativeAmount",
    )
    maximum_cumulative_number_of_payments: Optional[
        Annotated[int, Field(strict=True, ge=0)]
    ] = Field(
        default=None,
        description="Maximum cumulative number of payments",
        alias="maximumCumulativeNumberOfPayments",
    )
    periodic_limits: Optional[
        Annotated[List[VrpPeriodicLimit], Field(min_length=1)]
    ] = Field(default=None, alias="periodicLimits")
    recurring_payment_category: Optional[StrictStr] = Field(
        default=None,
        description="Payment Category with allowed values: ONGOING, SUBSCRIPTION",
        alias="recurringPaymentCategory",
    )
    __properties: ClassVar[List[str]] = [
        "maximumIndividualAmount",
        "maximumCumulativeAmount",
        "maximumCumulativeNumberOfPayments",
        "periodicLimits",
        "recurringPaymentCategory",
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
        if self.maximum_individual_amount:
            _dict["maximumIndividualAmount"] = self.maximum_individual_amount.to_dict()
        if self.maximum_cumulative_amount:
            _dict["maximumCumulativeAmount"] = self.maximum_cumulative_amount.to_dict()
        _items = []
        if self.periodic_limits:
            for _item_periodic_limits in self.periodic_limits:
                if _item_periodic_limits:
                    _items.append(_item_periodic_limits.to_dict())
            _dict["periodicLimits"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "maximumIndividualAmount": Amount.from_dict(
                    obj["maximumIndividualAmount"]
                )
                if obj.get("maximumIndividualAmount") is not None
                else None,
                "maximumCumulativeAmount": Amount.from_dict(
                    obj["maximumCumulativeAmount"]
                )
                if obj.get("maximumCumulativeAmount") is not None
                else None,
                "maximumCumulativeNumberOfPayments": obj.get(
                    "maximumCumulativeNumberOfPayments"
                ),
                "periodicLimits": [
                    VrpPeriodicLimit.from_dict(_item) for _item in obj["periodicLimits"]
                ]
                if obj.get("periodicLimits") is not None
                else None,
                "recurringPaymentCategory": obj.get("recurringPaymentCategory"),
            }
        )
        return _obj
