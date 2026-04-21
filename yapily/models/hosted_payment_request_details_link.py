import json
import pprint
from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_type_response import PaymentTypeResponse


class HostedPaymentRequestDetailsLink(BaseModel):
    """
    HostedPaymentRequestDetailsLink
    """

    reference: Annotated[
        StrictStr | None,
        Field(
            description="The payment reference or description. Limited to a maximum of 18 characters for UK institutions."
        ),
    ] = None
    context_type: Annotated[PaymentContextTypeResponse | None, Field(alias="contextType")] = None
    type: PaymentTypeResponse | None = None
    payee: PayeeDetailsResponse | None = None
    payer: PayerDetailsResponse | None = None
    amount_details: Annotated[AmountDetailsResponse | None, Field(alias="amountDetails")] = None
    payment_due_date: Annotated[
        date | None,
        Field(
            alias="paymentDueDate",
            description="The date that the payment is due. Displayed to the end user in the payment summary screen.",
        ),
    ] = None
    __properties = ["reference", "contextType", "type", "payee", "payer", "amountDetails", "paymentDueDate"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedPaymentRequestDetailsLink":
        """Create an instance of HostedPaymentRequestDetailsLink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_details
        if self.amount_details:
            _dict["amountDetails"] = self.amount_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedPaymentRequestDetailsLink":
        """Create an instance of HostedPaymentRequestDetailsLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedPaymentRequestDetailsLink.parse_obj(obj)

        return HostedPaymentRequestDetailsLink.parse_obj(
            {
                "reference": obj.get("reference"),
                "context_type": obj.get("contextType"),
                "type": obj.get("type"),
                "payee": PayeeDetailsResponse.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
                "payer": PayerDetailsResponse.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
                "amount_details": AmountDetailsResponse.from_dict(obj.get("amountDetails"))
                if obj.get("amountDetails") is not None
                else None,
                "payment_due_date": obj.get("paymentDueDate"),
            }
        )
