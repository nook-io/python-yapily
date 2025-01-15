# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from yapily.models.amount import Amount
from yapily.models.frequency_request import FrequencyRequest


class PeriodicPaymentRequest(BaseModel):
    """
    __Conditional__. Used to specify properties to define a periodic payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>  # noqa: E501
    """

    frequency: FrequencyRequest = Field(...)
    number_of_payments: Optional[StrictInt] = Field(
        default=None,
        alias="numberOfPayments",
        description="__Conditional__. Defines the total number of payments to be made.<br><br>This is required if `finalPaymentDateTime` is not specified and it is intended for the periodic payment have a fixed amount of payments.",
    )
    next_payment_date_time: Optional[datetime] = Field(
        default=None,
        alias="nextPaymentDateTime",
        description="__Conditional__. Defines when to start the recurring payment date and time. Specify this if you want the first payment to start on a different day than what the frequency object defines.",
    )
    next_payment_amount: Optional[Amount] = Field(
        default=None, alias="nextPaymentAmount"
    )
    final_payment_date_time: Optional[datetime] = Field(
        default=None,
        alias="finalPaymentDateTime",
        description="__Conditional__. Defines the final payment date and time. To create an open-ended periodic payment, do not specify this property.",
    )
    final_payment_amount: Optional[Amount] = Field(
        default=None, alias="finalPaymentAmount"
    )
    __properties = [
        "frequency",
        "numberOfPayments",
        "nextPaymentDateTime",
        "nextPaymentAmount",
        "finalPaymentDateTime",
        "finalPaymentAmount",
    ]

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
    def from_json(cls, json_str: str) -> PeriodicPaymentRequest:
        """Create an instance of PeriodicPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of frequency
        if self.frequency:
            _dict["frequency"] = self.frequency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next_payment_amount
        if self.next_payment_amount:
            _dict["nextPaymentAmount"] = self.next_payment_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of final_payment_amount
        if self.final_payment_amount:
            _dict["finalPaymentAmount"] = self.final_payment_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeriodicPaymentRequest:
        """Create an instance of PeriodicPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeriodicPaymentRequest.parse_obj(obj)

        _obj = PeriodicPaymentRequest.parse_obj(
            {
                "frequency": FrequencyRequest.from_dict(obj.get("frequency"))
                if obj.get("frequency") is not None
                else None,
                "number_of_payments": obj.get("numberOfPayments"),
                "next_payment_date_time": obj.get("nextPaymentDateTime"),
                "next_payment_amount": Amount.from_dict(obj.get("nextPaymentAmount"))
                if obj.get("nextPaymentAmount") is not None
                else None,
                "final_payment_date_time": obj.get("finalPaymentDateTime"),
                "final_payment_amount": Amount.from_dict(obj.get("finalPaymentAmount"))
                if obj.get("finalPaymentAmount") is not None
                else None,
            }
        )
        return _obj
