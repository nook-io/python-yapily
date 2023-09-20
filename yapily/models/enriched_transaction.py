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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class EnrichedTransaction(BaseModel):
    """
    Part of a financial profile for a User.  # noqa: E501
    """
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId", description="The id of the transaction")
    transaction_information: Optional[StrictStr] = Field(None, alias="transactionInformation", description="Information for the transaction")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The amount of the transaction")
    institution: Optional[StrictStr] = Field(None, description="The id of the institution")
    booking_date_time: Optional[datetime] = Field(None, alias="bookingDateTime", description="The datetime of the transaction")
    __properties = ["transactionId", "transactionInformation", "amount", "institution", "bookingDateTime"]

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
    def from_json(cls, json_str: str) -> EnrichedTransaction:
        """Create an instance of EnrichedTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnrichedTransaction:
        """Create an instance of EnrichedTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedTransaction.parse_obj(obj)

        _obj = EnrichedTransaction.parse_obj({
            "transaction_id": obj.get("transactionId"),
            "transaction_information": obj.get("transactionInformation"),
            "amount": obj.get("amount"),
            "institution": obj.get("institution"),
            "booking_date_time": obj.get("bookingDateTime")
        })
        return _obj


