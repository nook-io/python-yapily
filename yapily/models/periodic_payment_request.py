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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.frequency_request import FrequencyRequest
from typing import Set
from typing_extensions import Self


class PeriodicPaymentRequest(BaseModel):
    """
    __Conditional__. Used to specify properties to define a periodic payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>
    """  # noqa: E501

    frequency: FrequencyRequest
    number_of_payments: Optional[StrictInt] = Field(
        default=None,
        description="__Conditional__. Defines the total number of payments to be made.<br><br>This is required if `finalPaymentDateTime` is not specified and it is intended for the periodic payment have a fixed amount of payments.",
        alias="numberOfPayments",
    )
    next_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Defines when to start the recurring payment date and time. Specify this if you want the first payment to start on a different day than what the frequency object defines.",
        alias="nextPaymentDateTime",
    )
    next_payment_amount: Optional[Amount] = Field(
        default=None, alias="nextPaymentAmount"
    )
    final_payment_date_time: Optional[datetime] = Field(
        default=None,
        description="__Conditional__. Defines the final payment date and time. To create an open-ended periodic payment, do not specify this property.",
        alias="finalPaymentDateTime",
    )
    final_payment_amount: Optional[Amount] = Field(
        default=None, alias="finalPaymentAmount"
    )
    __properties: ClassVar[List[str]] = [
        "frequency",
        "numberOfPayments",
        "nextPaymentDateTime",
        "nextPaymentAmount",
        "finalPaymentDateTime",
        "finalPaymentAmount",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PeriodicPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PeriodicPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "frequency": FrequencyRequest.from_dict(obj["frequency"])
                if obj.get("frequency") is not None
                else None,
                "numberOfPayments": obj.get("numberOfPayments"),
                "nextPaymentDateTime": obj.get("nextPaymentDateTime"),
                "nextPaymentAmount": Amount.from_dict(obj["nextPaymentAmount"])
                if obj.get("nextPaymentAmount") is not None
                else None,
                "finalPaymentDateTime": obj.get("finalPaymentDateTime"),
                "finalPaymentAmount": Amount.from_dict(obj["finalPaymentAmount"])
                if obj.get("finalPaymentAmount") is not None
                else None,
            }
        )
        return _obj
