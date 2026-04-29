import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount
from yapily.models.payment_context_type import PaymentContextType


class SubmissionRequest(BaseModel):
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
    psu_authentication_method: Annotated[
        StrictStr,
        Field(
            alias="psuAuthenticationMethod",
            description="__Mandatory__. Chosen authentication method for submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED].",
        ),
    ]
    context_type: Annotated[PaymentContextType | None, Field(alias="contextType")] = None
    payment_amount: Annotated[Amount, Field(alias="paymentAmount")]
    __properties = ["paymentIdempotencyId", "psuAuthenticationMethod", "contextType", "paymentAmount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SubmissionRequest":
        """Create an instance of SubmissionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_amount
        if self.payment_amount:
            _dict["paymentAmount"] = self.payment_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SubmissionRequest":
        """Create an instance of SubmissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubmissionRequest.model_validate(obj)

        return SubmissionRequest.model_validate(
            {
                "payment_idempotency_id": obj.get("paymentIdempotencyId"),
                "psu_authentication_method": obj.get("psuAuthenticationMethod"),
                "context_type": obj.get("contextType"),
                "payment_amount": Amount.from_dict(obj.get("paymentAmount"))
                if obj.get("paymentAmount") is not None
                else None,
            }
        )
