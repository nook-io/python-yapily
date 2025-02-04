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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from yapily.models.rate_type_enum import RateTypeEnum


class ExchangeRateInformationResponse(BaseModel):
    """
    ExchangeRateInformationResponse
    """

    unit_currency: StrictStr = Field(
        default=...,
        alias="unitCurrency",
        description="__Mandatory__. The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is `GBP`.",
    )
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="__Optional__. The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.",
    )
    rate_type: RateTypeEnum = Field(default=..., alias="rateType")
    foreign_exchange_contract_reference: Optional[StrictStr] = Field(
        default=None,
        alias="foreignExchangeContractReference",
        description="__Optional__. The unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.",
    )
    exchange_rate_expiry_date: Optional[datetime] = Field(
        default=None, alias="exchangeRateExpiryDate"
    )
    __properties = [
        "unitCurrency",
        "rate",
        "rateType",
        "foreignExchangeContractReference",
        "exchangeRateExpiryDate",
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
    def from_json(cls, json_str: str) -> ExchangeRateInformationResponse:
        """Create an instance of ExchangeRateInformationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExchangeRateInformationResponse:
        """Create an instance of ExchangeRateInformationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExchangeRateInformationResponse.parse_obj(obj)

        _obj = ExchangeRateInformationResponse.parse_obj(
            {
                "unit_currency": obj.get("unitCurrency"),
                "rate": obj.get("rate"),
                "rate_type": obj.get("rateType"),
                "foreign_exchange_contract_reference": obj.get(
                    "foreignExchangeContractReference"
                ),
                "exchange_rate_expiry_date": obj.get("exchangeRateExpiryDate"),
            }
        )
        return _obj
