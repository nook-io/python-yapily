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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from yapily.models.frequency_enum_extended import FrequencyEnumExtended

class FrequencyRequest(BaseModel):
    """
    __Mandatory__. Defines the intervals at which payment should be made.  # noqa: E501
    """
    type: FrequencyEnumExtended = Field(...)
    interval_week: Optional[StrictInt] = Field(None, alias="intervalWeek", description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information")
    interval_month: Optional[StrictInt] = Field(None, alias="intervalMonth", description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information")
    execution_day: Optional[StrictInt] = Field(None, alias="executionDay", description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information")
    __properties = ["type", "intervalWeek", "intervalMonth", "executionDay"]

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
    def from_json(cls, json_str: str) -> FrequencyRequest:
        """Create an instance of FrequencyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FrequencyRequest:
        """Create an instance of FrequencyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrequencyRequest.parse_obj(obj)

        _obj = FrequencyRequest.parse_obj({
            "type": obj.get("type"),
            "interval_week": obj.get("intervalWeek"),
            "interval_month": obj.get("intervalMonth"),
            "execution_day": obj.get("executionDay")
        })
        return _obj


