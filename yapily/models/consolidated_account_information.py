from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_balance import AccountBalance
from typing import Set
from typing_extensions import Self


class ConsolidatedAccountInformation(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None,
        description="Identifier of the consolidated account. When used in Get Account Transactions calls, the transactions between the sub-accounts will not be reported",
    )
    account_balances: Optional[List[AccountBalance]] = Field(
        default=None, alias="accountBalances"
    )
    __properties: ClassVar[List[str]] = ["id", "accountBalances"]
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
        if self.account_balances:
            for _item_account_balances in self.account_balances:
                if _item_account_balances:
                    _items.append(_item_account_balances.to_dict())
            _dict["accountBalances"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "accountBalances": [
                    AccountBalance.from_dict(_item) for _item in obj["accountBalances"]
                ]
                if obj.get("accountBalances") is not None
                else None,
            }
        )
        return _obj
