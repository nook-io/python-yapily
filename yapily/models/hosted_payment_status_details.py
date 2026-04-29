import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.hosted_payment_iso_status import HostedPaymentIsoStatus
from yapily.models.payment_status import PaymentStatus


class HostedPaymentStatusDetails(BaseModel):
    """
    The status of the payment.  # noqa: E501
    """

    status: PaymentStatus | None = None
    status_update_date: Annotated[
        datetime | None, Field(alias="statusUpdateDate", description="Date and time the status was updated.")
    ] = None
    iso_status: Annotated[HostedPaymentIsoStatus | None, Field(alias="isoStatus")] = None
    __properties = ["status", "statusUpdateDate", "isoStatus"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedPaymentStatusDetails":
        """Create an instance of HostedPaymentStatusDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of iso_status
        if self.iso_status:
            _dict["isoStatus"] = self.iso_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedPaymentStatusDetails":
        """Create an instance of HostedPaymentStatusDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedPaymentStatusDetails.model_validate(obj)

        return HostedPaymentStatusDetails.model_validate(
            {
                "status": obj.get("status"),
                "status_update_date": obj.get("statusUpdateDate"),
                "iso_status": HostedPaymentIsoStatus.from_dict(obj.get("isoStatus"))
                if obj.get("isoStatus") is not None
                else None,
            }
        )
