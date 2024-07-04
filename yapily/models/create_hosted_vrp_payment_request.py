# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from yapily.models.amount import Amount

class CreateHostedVRPPaymentRequest(BaseModel):
    """
    __Mandatory__. The payment request object defining the details of the payment for execution under the Variable Recurring Payment consent.  # noqa: E501
    """
    payment_idempotency_id: StrictStr = Field(..., alias="paymentIdempotencyId", description="__Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.")
    amount: Amount = Field(...)
    __properties = ["paymentIdempotencyId", "amount"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateHostedVRPPaymentRequest:
        """Create an instance of CreateHostedVRPPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateHostedVRPPaymentRequest:
        """Create an instance of CreateHostedVRPPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateHostedVRPPaymentRequest.parse_obj(obj)

        _obj = CreateHostedVRPPaymentRequest.parse_obj({
            "payment_idempotency_id": obj.get("paymentIdempotencyId"),
            "amount": Amount.from_dict(obj.get("amount")) if obj.get("amount") is not None else None
        })
        return _obj


