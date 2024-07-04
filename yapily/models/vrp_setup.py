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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.amount import Amount
from yapily.models.hosted_vrp_limits import HostedVRPLimits
from yapily.models.hosted_vrp_payer_response import HostedVrpPayerResponse
from yapily.models.payee import Payee
from yapily.models.payment_risk import PaymentRisk

class VRPSetup(BaseModel):
    """
    VRPSetup
    """
    payer: Optional[HostedVrpPayerResponse] = None
    payee: Payee = Field(...)
    reference: Optional[StrictStr] = Field(None, description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.")
    limits: Optional[HostedVRPLimits] = None
    valid_from: Optional[datetime] = Field(None, alias="validFrom", description="__Optional__. Start date when the consent becomes valid.")
    valid_to: Optional[datetime] = Field(None, alias="validTo", description="__Optional__. End date when the consent expires and becomes invalid.")
    recurring_payment_category: Optional[StrictStr] = Field(None, alias="recurringPaymentCategory", description="The use-case for the VRP consent supported by the bank. Allowed values: <br>`ONGOING` <br>`SUBSCRIPTION`")
    initial_payment: Optional[Amount] = Field(None, alias="initialPayment")
    risk: Optional[PaymentRisk] = None
    __properties = ["payer", "payee", "reference", "limits", "validFrom", "validTo", "recurringPaymentCategory", "initialPayment", "risk"]

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
    def from_json(cls, json_str: str) -> VRPSetup:
        """Create an instance of VRPSetup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict['payer'] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict['payee'] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initial_payment
        if self.initial_payment:
            _dict['initialPayment'] = self.initial_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of risk
        if self.risk:
            _dict['risk'] = self.risk.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VRPSetup:
        """Create an instance of VRPSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VRPSetup.parse_obj(obj)

        _obj = VRPSetup.parse_obj({
            "payer": HostedVrpPayerResponse.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
            "payee": Payee.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
            "reference": obj.get("reference"),
            "limits": HostedVRPLimits.from_dict(obj.get("limits")) if obj.get("limits") is not None else None,
            "valid_from": obj.get("validFrom"),
            "valid_to": obj.get("validTo"),
            "recurring_payment_category": obj.get("recurringPaymentCategory"),
            "initial_payment": Amount.from_dict(obj.get("initialPayment")) if obj.get("initialPayment") is not None else None,
            "risk": PaymentRisk.from_dict(obj.get("risk")) if obj.get("risk") is not None else None
        })
        return _obj


