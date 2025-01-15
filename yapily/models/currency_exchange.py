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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr


class CurrencyExchange(BaseModel):
    """
    Provides details on the currrency exchange.  # noqa: E501
    """

    source_currency: Optional[StrictStr] = Field(
        default=None,
        alias="sourceCurrency",
        description="Currency from which an amount is to be converted.",
    )
    target_currency: Optional[StrictStr] = Field(
        default=None,
        alias="targetCurrency",
        description="Currency to which an amount is to be converted.",
    )
    unit_currency: Optional[StrictStr] = Field(
        default=None,
        alias="unitCurrency",
        description="The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.",
    )
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="exchangeRate",
        description="The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.",
    )
    __properties = ["sourceCurrency", "targetCurrency", "unitCurrency", "exchangeRate"]

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
    def from_json(cls, json_str: str) -> CurrencyExchange:
        """Create an instance of CurrencyExchange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrencyExchange:
        """Create an instance of CurrencyExchange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrencyExchange.parse_obj(obj)

        _obj = CurrencyExchange.parse_obj(
            {
                "source_currency": obj.get("sourceCurrency"),
                "target_currency": obj.get("targetCurrency"),
                "unit_currency": obj.get("unitCurrency"),
                "exchange_rate": obj.get("exchangeRate"),
            }
        )
        return _obj
