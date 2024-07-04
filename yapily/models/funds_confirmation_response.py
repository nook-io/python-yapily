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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.amount import Amount
from yapily.models.funds_available import FundsAvailable

class FundsConfirmationResponse(BaseModel):
    """
    FundsConfirmationResponse
    """
    id: Optional[StrictStr] = None
    reference: Optional[StrictStr] = Field(None, description="The payment reference or description. Limited to a maximum of 18 characters long.")
    payment_amount: Amount = Field(..., alias="paymentAmount")
    funds_available: FundsAvailable = Field(..., alias="fundsAvailable")
    __properties = ["id", "reference", "paymentAmount", "fundsAvailable"]

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
    def from_json(cls, json_str: str) -> FundsConfirmationResponse:
        """Create an instance of FundsConfirmationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_amount
        if self.payment_amount:
            _dict['paymentAmount'] = self.payment_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of funds_available
        if self.funds_available:
            _dict['fundsAvailable'] = self.funds_available.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FundsConfirmationResponse:
        """Create an instance of FundsConfirmationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FundsConfirmationResponse.parse_obj(obj)

        _obj = FundsConfirmationResponse.parse_obj({
            "id": obj.get("id"),
            "reference": obj.get("reference"),
            "payment_amount": Amount.from_dict(obj.get("paymentAmount")) if obj.get("paymentAmount") is not None else None,
            "funds_available": FundsAvailable.from_dict(obj.get("fundsAvailable")) if obj.get("fundsAvailable") is not None else None
        })
        return _obj


