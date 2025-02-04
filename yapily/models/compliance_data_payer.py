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
from yapily.models.compliance_data_business import ComplianceDataBusiness
from yapily.models.compliance_data_individual import ComplianceDataIndividual


class ComplianceDataPayer(BaseModel):
    """
    __Conditional__. Payer details required for compliance checks.  # noqa: E501
    """

    type: StrictStr = Field(
        default=...,
        description="The payer type. Allowed values: INDIVIDUAL, BUSINESS. The corresponding object must be included.",
    )
    individual: Optional[ComplianceDataIndividual] = None
    business: Optional[ComplianceDataBusiness] = None
    __properties = ["type", "individual", "business"]

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
    def from_json(cls, json_str: str) -> ComplianceDataPayer:
        """Create an instance of ComplianceDataPayer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of individual
        if self.individual:
            _dict["individual"] = self.individual.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business
        if self.business:
            _dict["business"] = self.business.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceDataPayer:
        """Create an instance of ComplianceDataPayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataPayer.parse_obj(obj)

        _obj = ComplianceDataPayer.parse_obj(
            {
                "type": obj.get("type"),
                "individual": ComplianceDataIndividual.from_dict(obj.get("individual"))
                if obj.get("individual") is not None
                else None,
                "business": ComplianceDataBusiness.from_dict(obj.get("business"))
                if obj.get("business") is not None
                else None,
            }
        )
        return _obj
