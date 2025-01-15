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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from yapily.models.enriched_transaction import EnrichedTransaction
from yapily.models.transaction_schedule import TransactionSchedule


class TerminatedTransactionStream(BaseModel):
    """
    Terminated transaction stream generated as part of the financial profile for a User.  # noqa: E501
    """

    name: Optional[StrictStr] = Field(
        default=None, description="The name of the TransactionStream"
    )
    transactions: Optional[conlist(EnrichedTransaction)] = Field(
        default=None, description="A list of Transactions from the transaction stream."
    )
    transaction_schedule: Optional[TransactionSchedule] = Field(
        default=None, alias="transactionSchedule"
    )
    schedule_consistency_score: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="scheduleConsistencyScore",
        description="The consistency of the transaction.  This is a number between 0 and 1 with 1 being the most consistent schedule.",
    )
    next_expected_transaction_date: Optional[date] = Field(
        default=None,
        alias="nextExpectedTransactionDate",
        description="When is the transaction expected to occur next.",
    )
    earliest_transaction_date: Optional[date] = Field(
        default=None,
        alias="earliestTransactionDate",
        description="When is the first recorded transaction date",
    )
    most_recent_transaction_date: Optional[date] = Field(
        default=None,
        alias="mostRecentTransactionDate",
        description="When is the most recent transaction date",
    )
    amount_consistency_score: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="amountConsistencyScore",
        description="The consistency of the amount of the transaction.  This is a number between 0 and 1 with 1 being the most consistent amount.",
    )
    average_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="averageAmount",
        description="The average amount of the transaction stream",
    )
    missed_transactions: Optional[StrictInt] = Field(
        default=None,
        alias="missedTransactions",
        description="Missed transactions of transaction stream",
    )
    __properties = [
        "name",
        "transactions",
        "transactionSchedule",
        "scheduleConsistencyScore",
        "nextExpectedTransactionDate",
        "earliestTransactionDate",
        "mostRecentTransactionDate",
        "amountConsistencyScore",
        "averageAmount",
        "missedTransactions",
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
    def from_json(cls, json_str: str) -> TerminatedTransactionStream:
        """Create an instance of TerminatedTransactionStream from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict["transactions"] = _items
        # override the default output from pydantic by calling `to_dict()` of transaction_schedule
        if self.transaction_schedule:
            _dict["transactionSchedule"] = self.transaction_schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TerminatedTransactionStream:
        """Create an instance of TerminatedTransactionStream from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TerminatedTransactionStream.parse_obj(obj)

        _obj = TerminatedTransactionStream.parse_obj(
            {
                "name": obj.get("name"),
                "transactions": [
                    EnrichedTransaction.from_dict(_item)
                    for _item in obj.get("transactions")
                ]
                if obj.get("transactions") is not None
                else None,
                "transaction_schedule": TransactionSchedule.from_dict(
                    obj.get("transactionSchedule")
                )
                if obj.get("transactionSchedule") is not None
                else None,
                "schedule_consistency_score": obj.get("scheduleConsistencyScore"),
                "next_expected_transaction_date": obj.get(
                    "nextExpectedTransactionDate"
                ),
                "earliest_transaction_date": obj.get("earliestTransactionDate"),
                "most_recent_transaction_date": obj.get("mostRecentTransactionDate"),
                "amount_consistency_score": obj.get("amountConsistencyScore"),
                "average_amount": obj.get("averageAmount"),
                "missed_transactions": obj.get("missedTransactions"),
            }
        )
        return _obj
