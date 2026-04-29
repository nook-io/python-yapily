import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount
from yapily.models.funds_available import FundsAvailable


class FundsConfirmationResponse(BaseModel):
    """
    FundsConfirmationResponse
    """

    id: StrictStr | None = None
    reference: Annotated[
        StrictStr | None,
        Field(description="The payment reference or description. Limited to a maximum of 18 characters long."),
    ] = None
    payment_amount: Annotated[Amount, Field(alias="paymentAmount")]
    funds_available: Annotated[FundsAvailable, Field(alias="fundsAvailable")]
    __properties = ["id", "reference", "paymentAmount", "fundsAvailable"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FundsConfirmationResponse":
        """Create an instance of FundsConfirmationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_amount
        if self.payment_amount:
            _dict["paymentAmount"] = self.payment_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of funds_available
        if self.funds_available:
            _dict["fundsAvailable"] = self.funds_available.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "FundsConfirmationResponse":
        """Create an instance of FundsConfirmationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FundsConfirmationResponse.model_validate(obj)

        return FundsConfirmationResponse.model_validate(
            {
                "id": obj.get("id"),
                "reference": obj.get("reference"),
                "payment_amount": Amount.from_dict(obj.get("paymentAmount"))
                if obj.get("paymentAmount") is not None
                else None,
                "funds_available": FundsAvailable.from_dict(obj.get("fundsAvailable"))
                if obj.get("fundsAvailable") is not None
                else None,
            }
        )
