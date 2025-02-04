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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.amount import Amount


class PaymentChargeDetails(BaseModel):
    """
    Details the charges that will apply to the payment.  # noqa: E501
    """

    charge_amount: Optional[Amount] = Field(default=None, alias="chargeAmount")
    charge_type: Optional[StrictStr] = Field(
        default=None,
        alias="chargeType",
        description="__Mandatory__. Specifies the nature of the transaction charge e.g. (Bank transfer fees).",
    )
    charge_to: Optional[StrictStr] = Field(
        default=None,
        alias="chargeTo",
        description="__Mandatory__. States which party of the payment bears the charges.",
    )
    __properties = ["chargeAmount", "chargeType", "chargeTo"]

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
    def from_json(cls, json_str: str) -> PaymentChargeDetails:
        """Create an instance of PaymentChargeDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of charge_amount
        if self.charge_amount:
            _dict["chargeAmount"] = self.charge_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentChargeDetails:
        """Create an instance of PaymentChargeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentChargeDetails.parse_obj(obj)

        _obj = PaymentChargeDetails.parse_obj(
            {
                "charge_amount": Amount.from_dict(obj.get("chargeAmount"))
                if obj.get("chargeAmount") is not None
                else None,
                "charge_type": obj.get("chargeType"),
                "charge_to": obj.get("chargeTo"),
            }
        )
        return _obj
