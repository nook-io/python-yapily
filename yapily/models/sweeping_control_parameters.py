import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount
from yapily.models.sweeping_periodic_limits import SweepingPeriodicLimits


class SweepingControlParameters(BaseModel):
    """
    Define the restrictions and limits for payment orders as part of Sweeping VRP consent  # noqa: E501
    """

    psu_authentication_methods: Annotated[
        list[StrictStr],
        Field(
            alias="psuAuthenticationMethods",
            description="__Mandatory__. Defines the authentication method(s) allowed in payment submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED].",
        ),
    ]
    periodic_limits: Annotated[list[SweepingPeriodicLimits], Field(alias="periodicLimits")]
    max_amount_per_payment: Annotated[
        Amount,
        Field(alias="maxAmountPerPayment", description="__Mandatory__. Max amount that can be submitted per payment."),
    ]
    valid_from: Annotated[
        datetime | None,
        Field(alias="validFrom", description="__Optional__. Start date when the consent becomes valid."),
    ] = None
    valid_to: Annotated[
        datetime | None,
        Field(alias="validTo", description="__Optional__. End date when the consent expires and becomes invalid."),
    ] = None
    __properties = ["psuAuthenticationMethods", "periodicLimits", "maxAmountPerPayment", "validFrom", "validTo"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SweepingControlParameters":
        """Create an instance of SweepingControlParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in periodic_limits (list)
        _items = []
        if self.periodic_limits:
            for _item in self.periodic_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict["periodicLimits"] = _items
        # override the default output from pydantic by calling `to_dict()` of max_amount_per_payment
        if self.max_amount_per_payment:
            _dict["maxAmountPerPayment"] = self.max_amount_per_payment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SweepingControlParameters":
        """Create an instance of SweepingControlParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SweepingControlParameters.model_validate(obj)

        return SweepingControlParameters.model_validate(
            {
                "psu_authentication_methods": obj.get("psuAuthenticationMethods"),
                "periodic_limits": [SweepingPeriodicLimits.from_dict(_item) for _item in obj.get("periodicLimits")]
                if obj.get("periodicLimits") is not None
                else None,
                "max_amount_per_payment": Amount.from_dict(obj.get("maxAmountPerPayment"))
                if obj.get("maxAmountPerPayment") is not None
                else None,
                "valid_from": obj.get("validFrom"),
                "valid_to": obj.get("validTo"),
            }
        )
