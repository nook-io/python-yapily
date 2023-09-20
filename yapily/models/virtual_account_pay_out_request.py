# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.virtual_account_payment_amount import VirtualAccountPaymentAmount

class VirtualAccountPayOutRequest(BaseModel):
    """
    VirtualAccountPayOutRequest
    """
    account_id: StrictStr = Field(..., alias="accountId", description="Unique id of the source / payer account")
    amount: VirtualAccountPaymentAmount = Field(...)
    reference: StrictStr = Field(..., description="Reference to be associated with the payment. This will be appear on the beneficiary's bank statement")
    beneficiary_id: StrictStr = Field(..., alias="beneficiaryId", description="Unique id of the beneficiary to whom the payment will be made")
    payment_scheme: StrictStr = Field(..., alias="paymentScheme", description="Method of settlement to complete the payment. One of: <br> FASTER_PAYMENTS <br> SEPA_CREDIT <br> SEPA_INSTANT <br> SWIFT <br> SWIFT_EXPRESS <br> CHAPS <br> IAT <br> WIRE")
    payment_date: Optional[date] = Field(None, alias="paymentDate", description="Date on which a payment instruction will be executed, that must be in the future")
    __properties = ["accountId", "amount", "reference", "beneficiaryId", "paymentScheme", "paymentDate"]

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
    def from_json(cls, json_str: str) -> VirtualAccountPayOutRequest:
        """Create an instance of VirtualAccountPayOutRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> VirtualAccountPayOutRequest:
        """Create an instance of VirtualAccountPayOutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VirtualAccountPayOutRequest.parse_obj(obj)

        _obj = VirtualAccountPayOutRequest.parse_obj({
            "account_id": obj.get("accountId"),
            "amount": VirtualAccountPaymentAmount.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "reference": obj.get("reference"),
            "beneficiary_id": obj.get("beneficiaryId"),
            "payment_scheme": obj.get("paymentScheme"),
            "payment_date": obj.get("paymentDate")
        })
        return _obj


