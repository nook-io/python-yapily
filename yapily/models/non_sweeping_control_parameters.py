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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from yapily.models.amount import Amount
from yapily.models.non_sweeping_periodic_limits import NonSweepingPeriodicLimits

class NonSweepingControlParameters(BaseModel):
    """
    Define the restrictions and limits for payment orders as part of Non-Sweeping VRP consent  # noqa: E501
    """
    psu_authentication_methods: conlist(StrictStr) = Field(..., alias="psuAuthenticationMethods", description="__Mandatory__. Defines the authentication method(s) allowed in payment submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED].")
    periodic_limits: conlist(NonSweepingPeriodicLimits) = Field(..., alias="periodicLimits")
    max_amount_per_payment: Amount = Field(..., alias="maxAmountPerPayment")
    max_cumulative_amount: Optional[Amount] = Field(None, alias="maxCumulativeAmount")
    max_cumulative_number_of_payments: Optional[StrictInt] = Field(None, alias="maxCumulativeNumberOfPayments", description="__Optional__. Max number of payments that can be submitted under this consent.")
    valid_from: Optional[datetime] = Field(None, alias="validFrom", description="__Optional__. Start date when the consent becomes valid.")
    valid_to: Optional[datetime] = Field(None, alias="validTo", description="__Optional__. End date when the consent expires and becomes invalid.")
    __properties = ["psuAuthenticationMethods", "periodicLimits", "maxAmountPerPayment", "maxCumulativeAmount", "maxCumulativeNumberOfPayments", "validFrom", "validTo"]

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
    def from_json(cls, json_str: str) -> NonSweepingControlParameters:
        """Create an instance of NonSweepingControlParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in periodic_limits (list)
        _items = []
        if self.periodic_limits:
            for _item in self.periodic_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['periodicLimits'] = _items
        # override the default output from pydantic by calling `to_dict()` of max_amount_per_payment
        if self.max_amount_per_payment:
            _dict['maxAmountPerPayment'] = self.max_amount_per_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_cumulative_amount
        if self.max_cumulative_amount:
            _dict['maxCumulativeAmount'] = self.max_cumulative_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonSweepingControlParameters:
        """Create an instance of NonSweepingControlParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonSweepingControlParameters.parse_obj(obj)

        _obj = NonSweepingControlParameters.parse_obj({
            "psu_authentication_methods": obj.get("psuAuthenticationMethods"),
            "periodic_limits": [NonSweepingPeriodicLimits.from_dict(_item) for _item in obj.get("periodicLimits")] if obj.get("periodicLimits") is not None else None,
            "max_amount_per_payment": Amount.from_dict(obj.get("maxAmountPerPayment")) if obj.get("maxAmountPerPayment") is not None else None,
            "max_cumulative_amount": Amount.from_dict(obj.get("maxCumulativeAmount")) if obj.get("maxCumulativeAmount") is not None else None,
            "max_cumulative_number_of_payments": obj.get("maxCumulativeNumberOfPayments"),
            "valid_from": obj.get("validFrom"),
            "valid_to": obj.get("validTo")
        })
        return _obj


