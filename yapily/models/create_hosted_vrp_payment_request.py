import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount


class CreateHostedVRPPaymentRequest(BaseModel):
    """
    __Mandatory__. The payment request object defining the details of the payment for execution under the Variable Recurring Payment consent.  # noqa: E501
    """

    payment_idempotency_id: Annotated[
        StrictStr,
        Field(
            alias="paymentIdempotencyId",
            description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        ),
    ]
    amount: Annotated[Amount, Field()]
    __properties = ["paymentIdempotencyId", "amount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CreateHostedVRPPaymentRequest":
        """Create an instance of CreateHostedVRPPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict["amount"] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "CreateHostedVRPPaymentRequest":
        """Create an instance of CreateHostedVRPPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateHostedVRPPaymentRequest.model_validate(obj)

        return CreateHostedVRPPaymentRequest.model_validate(
            {
                "payment_idempotency_id": obj.get("paymentIdempotencyId"),
                "amount": Amount.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            }
        )
