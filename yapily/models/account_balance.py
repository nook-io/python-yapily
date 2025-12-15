from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_balance_type import AccountBalanceType
from yapily.models.amount import Amount
from yapily.models.credit_line import CreditLine
from typing import Set
from typing_extensions import Self


class AccountBalance(BaseModel):
    type: Optional[AccountBalanceType] = None
    date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of the reported balance.",
        alias="dateTime",
    )
    balance_amount: Optional[Amount] = Field(default=None, alias="balanceAmount")
    credit_line_included: Optional[StrictBool] = Field(
        default=None,
        description="_Optional_. Indicates whether any credit lines are included in the balance.",
        alias="creditLineIncluded",
    )
    credit_lines: Optional[List[CreditLine]] = Field(
        default=None,
        description="_Optional_. Specifies the type of balance.",
        alias="creditLines",
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "dateTime",
        "balanceAmount",
        "creditLineIncluded",
        "creditLines",
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
        if self.balance_amount:
            _dict["balanceAmount"] = self.balance_amount.to_dict()
        _items = []
        if self.credit_lines:
            for _item_credit_lines in self.credit_lines:
                if _item_credit_lines:
                    _items.append(_item_credit_lines.to_dict())
            _dict["creditLines"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "dateTime": obj.get("dateTime"),
                "balanceAmount": Amount.from_dict(obj["balanceAmount"])
                if obj.get("balanceAmount") is not None
                else None,
                "creditLineIncluded": obj.get("creditLineIncluded"),
                "creditLines": [
                    CreditLine.from_dict(_item) for _item in obj["creditLines"]
                ]
                if obj.get("creditLines") is not None
                else None,
            }
        )
        return _obj
