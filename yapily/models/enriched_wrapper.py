from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from yapily.models.terminated_transaction_stream import TerminatedTransactionStream
from yapily.models.transaction_stream import TransactionStream
from typing import Optional, Set
from typing_extensions import Self


class EnrichedWrapper(BaseModel):
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
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        _items = []
        if self.income_streams:
            for _item_income_streams in self.income_streams:
                if _item_income_streams:
                    _items.append(_item_income_streams.to_dict())
            _dict["incomeStreams"] = _items
        _items = []
        if self.expenditure_streams:
            for _item_expenditure_streams in self.expenditure_streams:
                if _item_expenditure_streams:
                    _items.append(_item_expenditure_streams.to_dict())
            _dict["expenditureStreams"] = _items
        _items = []
        if self.recently_terminated_income_streams:
            for (
                _item_recently_terminated_income_streams
            ) in self.recently_terminated_income_streams:
                if _item_recently_terminated_income_streams:
                    _items.append(_item_recently_terminated_income_streams.to_dict())
            _dict["recentlyTerminatedIncomeStreams"] = _items
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
