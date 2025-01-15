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

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt


class EnrichedPredictedBalance(BaseModel):
    """
    A list of Predicted Account Balances for future date range.  # noqa: E501
    """

    var_date: Optional[date] = Field(
        default=None,
        alias="date",
        description="The date for which Balance amount is predicted.",
    )
    median_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="medianBalance",
        description="The median Balance amount for a future date.",
    )
    var_90percentile_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="90percentileBalance",
        description="The 90th percentile Balance amount for a future date.",
    )
    var_10percentile_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="10percentileBalance",
        description="The 10th percentile Balance amount for a future date.",
    )
    __properties = [
        "date",
        "medianBalance",
        "90percentileBalance",
        "10percentileBalance",
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
    def from_json(cls, json_str: str) -> EnrichedPredictedBalance:
        """Create an instance of EnrichedPredictedBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnrichedPredictedBalance:
        """Create an instance of EnrichedPredictedBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedPredictedBalance.parse_obj(obj)

        _obj = EnrichedPredictedBalance.parse_obj(
            {
                "var_date": obj.get("date"),
                "median_balance": obj.get("medianBalance"),
                "var_90percentile_balance": obj.get("90percentileBalance"),
                "var_10percentile_balance": obj.get("10percentileBalance"),
            }
        )
        return _obj
