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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from yapily.models.enriched_transaction import EnrichedTransaction
from yapily.models.transaction_schedule import TransactionSchedule
from typing import Set
from typing_extensions import Self


class TransactionStream(BaseModel):
    """
    Lists all possible transaction streams identified for the `Application User`.
    """  # noqa: E501

    name: Optional[StrictStr] = Field(
        default=None, description="The name of the Transaction Stream."
    )
    transactions: Optional[List[EnrichedTransaction]] = Field(
        default=None,
        description="A list of transaction details, identified by Yapily data services.",
    )
    transaction_schedule: Optional[TransactionSchedule] = Field(
        default=None, alias="transactionSchedule"
    )
    schedule_consistency_score: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The consistency of the transaction.  This is a number between 0 and 1 with 1 being the most consistent schedule.",
        alias="scheduleConsistencyScore",
    )
    next_expected_transaction_date: Optional[date] = Field(
        default=None,
        description="When is the transaction expected to occur next.",
        alias="nextExpectedTransactionDate",
    )
    earliest_transaction_date: Optional[date] = Field(
        default=None,
        description="When is the first recorded transaction date",
        alias="earliestTransactionDate",
    )
    most_recent_transaction_date: Optional[date] = Field(
        default=None,
        description="When is the most recent transaction date",
        alias="mostRecentTransactionDate",
    )
    amount_consistency_score: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The consistency of the amount of the transaction.  This is a number between 0 and 1 with 1 being the most consistent amount.",
        alias="amountConsistencyScore",
    )
    average_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The average amount of the transaction stream",
        alias="averageAmount",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "transactions",
        "transactionSchedule",
        "scheduleConsistencyScore",
        "nextExpectedTransactionDate",
        "earliestTransactionDate",
        "mostRecentTransactionDate",
        "amountConsistencyScore",
        "averageAmount",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionStream from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict["transactions"] = _items
        # override the default output from pydantic by calling `to_dict()` of transaction_schedule
        if self.transaction_schedule:
            _dict["transactionSchedule"] = self.transaction_schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionStream from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "transactions": [
                    EnrichedTransaction.from_dict(_item)
                    for _item in obj["transactions"]
                ]
                if obj.get("transactions") is not None
                else None,
                "transactionSchedule": TransactionSchedule.from_dict(
                    obj["transactionSchedule"]
                )
                if obj.get("transactionSchedule") is not None
                else None,
                "scheduleConsistencyScore": obj.get("scheduleConsistencyScore"),
                "nextExpectedTransactionDate": obj.get("nextExpectedTransactionDate"),
                "earliestTransactionDate": obj.get("earliestTransactionDate"),
                "mostRecentTransactionDate": obj.get("mostRecentTransactionDate"),
                "amountConsistencyScore": obj.get("amountConsistencyScore"),
                "averageAmount": obj.get("averageAmount"),
            }
        )
        return _obj
