import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount import Amount
from yapily.models.payee import Payee


class SubmissionDetails(BaseModel):
    """
    __Mandatory__. The payment submission object defining the details of the payment instruction to be executed under the Variable Recurring Payment.  # noqa: E501
    """

    reference: Annotated[
        StrictStr | None,
        Field(
            description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long."
        ),
    ] = None
    payee: Annotated[Payee, Field()]
    payment_amount: Annotated[Amount, Field(alias="paymentAmount")]
    __properties = ["reference", "payee", "paymentAmount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SubmissionDetails":
        """Create an instance of SubmissionDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_amount
        if self.payment_amount:
            _dict["paymentAmount"] = self.payment_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SubmissionDetails":
        """Create an instance of SubmissionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubmissionDetails.model_validate(obj)

        return SubmissionDetails.model_validate(
            {
                "reference": obj.get("reference"),
                "payee": Payee.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
                "payment_amount": Amount.from_dict(obj.get("paymentAmount"))
                if obj.get("paymentAmount") is not None
                else None,
            }
        )
