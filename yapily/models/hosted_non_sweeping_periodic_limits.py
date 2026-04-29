import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount


class HostedNonSweepingPeriodicLimits(BaseModel):
    """
    HostedNonSweepingPeriodicLimits
    """

    max_amount: Annotated[
        Amount,
        Field(
            alias="maxAmount",
            description="__Mandatory__. Maximum amount that can be specified in all payment instructions in a given period under this VRP consent. If the Alignment is Calendar, the limit is pro-rated in the first period to the remaining number of days.",
        ),
    ]
    frequency: Annotated[
        StrictStr,
        Field(
            description="__Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [MONTHLY]."
        ),
    ]
    alignment: Annotated[
        StrictStr,
        Field(
            description="__Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question."
        ),
    ]
    __properties = ["maxAmount", "frequency", "alignment"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedNonSweepingPeriodicLimits":
        """Create an instance of HostedNonSweepingPeriodicLimits from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of max_amount
        if self.max_amount:
            _dict["maxAmount"] = self.max_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedNonSweepingPeriodicLimits":
        """Create an instance of HostedNonSweepingPeriodicLimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedNonSweepingPeriodicLimits.model_validate(obj)

        return HostedNonSweepingPeriodicLimits.model_validate(
            {
                "max_amount": Amount.from_dict(obj.get("maxAmount")) if obj.get("maxAmount") is not None else None,
                "frequency": obj.get("frequency"),
                "alignment": obj.get("alignment"),
            }
        )
