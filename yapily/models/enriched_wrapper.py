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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from yapily.models.terminated_transaction_stream import TerminatedTransactionStream
from yapily.models.transaction_stream import TransactionStream
from typing import Optional, Set
from typing_extensions import Self


class EnrichedWrapper(BaseModel):
    """
    Details of income and expenditure streams, identified by Yapily data services.
    """  # noqa: E501

    income_streams: List[TransactionStream] = Field(
        description="Lists all possible income streams identified for the `Application User`.",
        alias="incomeStreams",
    )
    expenditure_streams: List[TransactionStream] = Field(
        description="Lists all possible expenditure streams identified for the `Application User`.",
        alias="expenditureStreams",
    )
    recently_terminated_income_streams: List[TerminatedTransactionStream] = Field(
        description="A list of terminated transaction income streams",
        alias="recentlyTerminatedIncomeStreams",
    )
    recently_terminated_expenditure_streams: List[TerminatedTransactionStream] = Field(
        description="A list of terminated transaction expenditure streams",
        alias="recentlyTerminatedExpenditureStreams",
    )
    __properties: ClassVar[List[str]] = [
        "incomeStreams",
        "expenditureStreams",
        "recentlyTerminatedIncomeStreams",
        "recentlyTerminatedExpenditureStreams",
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
        """Create an instance of EnrichedWrapper from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in income_streams (list)
        _items = []
        if self.income_streams:
            for _item_income_streams in self.income_streams:
                if _item_income_streams:
                    _items.append(_item_income_streams.to_dict())
            _dict["incomeStreams"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expenditure_streams (list)
        _items = []
        if self.expenditure_streams:
            for _item_expenditure_streams in self.expenditure_streams:
                if _item_expenditure_streams:
                    _items.append(_item_expenditure_streams.to_dict())
            _dict["expenditureStreams"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recently_terminated_income_streams (list)
        _items = []
        if self.recently_terminated_income_streams:
            for (
                _item_recently_terminated_income_streams
            ) in self.recently_terminated_income_streams:
                if _item_recently_terminated_income_streams:
                    _items.append(_item_recently_terminated_income_streams.to_dict())
            _dict["recentlyTerminatedIncomeStreams"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recently_terminated_expenditure_streams (list)
        _items = []
        if self.recently_terminated_expenditure_streams:
            for (
                _item_recently_terminated_expenditure_streams
            ) in self.recently_terminated_expenditure_streams:
                if _item_recently_terminated_expenditure_streams:
                    _items.append(
                        _item_recently_terminated_expenditure_streams.to_dict()
                    )
            _dict["recentlyTerminatedExpenditureStreams"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnrichedWrapper from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "incomeStreams": [
                    TransactionStream.from_dict(_item) for _item in obj["incomeStreams"]
                ]
                if obj.get("incomeStreams") is not None
                else None,
                "expenditureStreams": [
                    TransactionStream.from_dict(_item)
                    for _item in obj["expenditureStreams"]
                ]
                if obj.get("expenditureStreams") is not None
                else None,
                "recentlyTerminatedIncomeStreams": [
                    TerminatedTransactionStream.from_dict(_item)
                    for _item in obj["recentlyTerminatedIncomeStreams"]
                ]
                if obj.get("recentlyTerminatedIncomeStreams") is not None
                else None,
                "recentlyTerminatedExpenditureStreams": [
                    TerminatedTransactionStream.from_dict(_item)
                    for _item in obj["recentlyTerminatedExpenditureStreams"]
                ]
                if obj.get("recentlyTerminatedExpenditureStreams") is not None
                else None,
            }
        )
        return _obj
