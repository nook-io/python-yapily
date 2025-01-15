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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from yapily.models.beneficiary_payee import BeneficiaryPayee


class Beneficiary(BaseModel):
    """
    Account information belonging to the target beneficiary (person/ business).  # noqa: E501
    """

    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the `beneficiary`."
    )
    reference: Optional[StrictStr] = Field(
        default=None,
        description="A creditor reference that is requested to be used for all payment instructions to this beneficiary.",
    )
    payee: Optional[BeneficiaryPayee] = None
    trusted: Optional[StrictBool] = Field(
        default=None,
        description="Indicates whether the account owner has stated that this beneficiary should be trusted. This often results in reduced authentication and authorisation requirements on payments to the beneficiary.",
    )
    __properties = ["id", "reference", "payee", "trusted"]

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
    def from_json(cls, json_str: str) -> Beneficiary:
        """Create an instance of Beneficiary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Beneficiary:
        """Create an instance of Beneficiary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Beneficiary.parse_obj(obj)

        _obj = Beneficiary.parse_obj(
            {
                "id": obj.get("id"),
                "reference": obj.get("reference"),
                "payee": BeneficiaryPayee.from_dict(obj.get("payee"))
                if obj.get("payee") is not None
                else None,
                "trusted": obj.get("trusted"),
            }
        )
        return _obj
