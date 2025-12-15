from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from yapily.models.account_identification import AccountIdentification
from typing import Optional, Set
from typing_extensions import Self


class PayerDetails(BaseModel):
    account_identifications: List[AccountIdentification] = Field(
        description="__Mandatory__. The account identifications that identify the `Payer` bank account.",
        alias="accountIdentifications",
    )
    __properties: ClassVar[List[str]] = ["accountIdentifications"]
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
        if self.account_identifications:
            for _item_account_identifications in self.account_identifications:
                if _item_account_identifications:
                    _items.append(_item_account_identifications.to_dict())
            _dict["accountIdentifications"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "accountIdentifications": [
                    AccountIdentification.from_dict(_item)
                    for _item in obj["accountIdentifications"]
                ]
                if obj.get("accountIdentifications") is not None
                else None
            }
        )
        return _obj
