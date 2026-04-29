import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount
from yapily.models.vrp_periodic_limit import VrpPeriodicLimit


class VrpConfiguration(BaseModel):
    """
    VrpConfiguration
    """

    maximum_individual_amount: Annotated[
        Amount | None, Field(alias="maximumIndividualAmount", description="Maximum amount per transaction")
    ] = None
    maximum_cumulative_amount: Annotated[
        Amount | None, Field(alias="maximumCumulativeAmount", description="Maximum cumulative amount")
    ] = None
    maximum_cumulative_number_of_payments: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None,
        Field(alias="maximumCumulativeNumberOfPayments", description="Maximum cumulative number of payments"),
    ] = None
    periodic_limits: Annotated[
        Annotated[list[VrpPeriodicLimit], Field(min_length=1)] | None, Field(alias="periodicLimits")
    ] = None
    recurring_payment_category: Annotated[
        StrictStr | None,
        Field(
            alias="recurringPaymentCategory", description="Payment Category with allowed values: ONGOING, SUBSCRIPTION"
        ),
    ] = None
    __properties = [
        "maximumIndividualAmount",
        "maximumCumulativeAmount",
        "maximumCumulativeNumberOfPayments",
        "periodicLimits",
        "recurringPaymentCategory",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "VrpConfiguration":
        """Create an instance of VrpConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of maximum_individual_amount
        if self.maximum_individual_amount:
            _dict["maximumIndividualAmount"] = self.maximum_individual_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum_cumulative_amount
        if self.maximum_cumulative_amount:
            _dict["maximumCumulativeAmount"] = self.maximum_cumulative_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in periodic_limits (list)
        _items = []
        if self.periodic_limits:
            for _item in self.periodic_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict["periodicLimits"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "VrpConfiguration":
        """Create an instance of VrpConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VrpConfiguration.model_validate(obj)

        return VrpConfiguration.model_validate(
            {
                "maximum_individual_amount": Amount.from_dict(obj.get("maximumIndividualAmount"))
                if obj.get("maximumIndividualAmount") is not None
                else None,
                "maximum_cumulative_amount": Amount.from_dict(obj.get("maximumCumulativeAmount"))
                if obj.get("maximumCumulativeAmount") is not None
                else None,
                "maximum_cumulative_number_of_payments": obj.get("maximumCumulativeNumberOfPayments"),
                "periodic_limits": [VrpPeriodicLimit.from_dict(_item) for _item in obj.get("periodicLimits")]
                if obj.get("periodicLimits") is not None
                else None,
                "recurring_payment_category": obj.get("recurringPaymentCategory"),
            }
        )
