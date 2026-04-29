import json
import pprint
from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.hosted_amount_details import HostedAmountDetails
from yapily.models.payee import Payee
from yapily.models.payer import Payer
from yapily.models.payment_context_type import PaymentContextType
from yapily.models.payment_type import PaymentType


class HostedPaymentRequestDetails(BaseModel):
    """
    Details of the payment.  # noqa: E501
    """

    payment_idempotency_id: Annotated[
        StrictStr,
        Field(
            alias="paymentIdempotencyId",
            description="A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.",
        ),
    ]
    reference: Annotated[
        StrictStr | None,
        Field(
            description="The payment reference or description. Limited to a maximum of 18 characters for UK institutions."
        ),
    ] = None
    context_type: Annotated[PaymentContextType | None, Field(alias="contextType")] = None
    type: Annotated[PaymentType, Field()]
    payee: Annotated[Payee, Field()]
    payer: Payer | None = None
    amount_details: Annotated[HostedAmountDetails, Field(alias="amountDetails")]
    payment_due_date: Annotated[
        date | None,
        Field(
            alias="paymentDueDate",
            description="The date that the payment is due. Displayed to the end user in the payment summary screen.",
        ),
    ] = None
    __properties = [
        "paymentIdempotencyId",
        "reference",
        "contextType",
        "type",
        "payee",
        "payer",
        "amountDetails",
        "paymentDueDate",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedPaymentRequestDetails":
        """Create an instance of HostedPaymentRequestDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
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
    def from_dict(cls, obj: dict) -> "HostedPaymentRequestDetails":
        """Create an instance of HostedPaymentRequestDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedPaymentRequestDetails.model_validate(obj)

        return HostedPaymentRequestDetails.model_validate(
            {
                "payment_idempotency_id": obj.get("paymentIdempotencyId"),
                "reference": obj.get("reference"),
                "context_type": obj.get("contextType"),
                "type": obj.get("type"),
                "payee": Payee.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
                "payer": Payer.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
                "amount_details": HostedAmountDetails.from_dict(obj.get("amountDetails"))
                if obj.get("amountDetails") is not None
                else None,
                "payment_due_date": obj.get("paymentDueDate"),
            }
        )
