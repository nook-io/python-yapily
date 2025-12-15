from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_balance import AccountBalance
from yapily.models.amount import Amount
from typing import Set
from typing_extensions import Self


class Balances(BaseModel):
    main_balance_amount: Optional[Amount] = Field(
        default=None, alias="mainBalanceAmount"
    )
    balances: Optional[List[AccountBalance]] = None
    __properties: ClassVar[List[str]] = ["mainBalanceAmount", "balances"]
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
        if self.main_balance_amount:
            _dict["mainBalanceAmount"] = self.main_balance_amount.to_dict()
        _items = []
        if self.balances:
            for _item_balances in self.balances:
                if _item_balances:
                    _items.append(_item_balances.to_dict())
            _dict["balances"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "mainBalanceAmount": Amount.from_dict(obj["mainBalanceAmount"])
                if obj.get("mainBalanceAmount") is not None
                else None,
                "balances": [
                    AccountBalance.from_dict(_item) for _item in obj["balances"]
                ]
                if obj.get("balances") is not None
                else None,
            }
        )
        return _obj
