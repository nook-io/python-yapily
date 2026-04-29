import json
import pprint
import re
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr, StringConstraints, field_validator

from yapily.models.payment_request import PaymentRequest


class SubmitBulkPaymentRequest(BaseModel):
    """
    The payment request object defining the details of the bulk payment  # noqa: E501
    """

    idempotency_id: Annotated[
        Annotated[str, StringConstraints(strict=True, max_length=40, min_length=1)] | None,
        Field(
            alias="idempotencyId",
            description="__Optional__. An alphanumeric string (1-40 chars) used for idempotency. Unique per consent ID for 24 hours. Prevents duplicate bulk file payment submissions.",
        ),
    ] = None
    payments: Annotated[
        list[PaymentRequest],
        Field(description="__Mandatory__. The array of `PaymentRequest` objects to initiate in the bulk payment."),
    ]
    originator_identification_number: Annotated[
        StrictStr | None,
        Field(
            alias="originatorIdentificationNumber",
            description="__Conditional__. The identification number of the originator.<ul><li>Mandatory for AIB bulk payments</li></ul>",
        ),
    ] = None
    execution_date_time: Annotated[
        datetime | None,
        Field(
            alias="executionDateTime",
            description="__Optional__. Used to schedule the bulk payment to be executed at a future date if supported by the `Institution`.",
        ),
    ] = None
    __properties = ["idempotencyId", "payments", "originatorIdentificationNumber", "executionDateTime"]

    @field_validator("idempotency_id")
    @classmethod
    def idempotency_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S{1,40}$", value):
            raise ValueError(r"must validate the regular expression /^\S{1,40}$/")
        return value

    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SubmitBulkPaymentRequest":
        """Create an instance of SubmitBulkPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["payments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SubmitBulkPaymentRequest":
        """Create an instance of SubmitBulkPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubmitBulkPaymentRequest.model_validate(obj)

        return SubmitBulkPaymentRequest.model_validate(
            {
                "idempotency_id": obj.get("idempotencyId"),
                "payments": [PaymentRequest.from_dict(_item) for _item in obj.get("payments")]
                if obj.get("payments") is not None
                else None,
                "originator_identification_number": obj.get("originatorIdentificationNumber"),
                "execution_date_time": obj.get("executionDateTime"),
            }
        )
