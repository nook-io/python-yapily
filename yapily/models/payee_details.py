from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from yapily.models.account_identification import AccountIdentification
from typing import Optional, Set
from typing_extensions import Self


class PayeeDetails(BaseModel):
    name: StrictStr = Field(
        description="__Mandatory__. The account holder name of the beneficiary."
    )
    account_identifications: List[AccountIdentification] = Field(
        description="__Mandatory__. The account identifications that identify the `Payee` bank account.",
        alias="accountIdentifications",
    )
    country: StrictStr = Field(
        description="__Conditional__. The 2-letter ISO 3166 country code for the address. <br><br>An `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to make a payment"
    )
    __properties: ClassVar[List[str]] = ["name", "accountIdentifications", "country"]
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
                "name": obj.get("name"),
                "accountIdentifications": [
                    AccountIdentification.from_dict(_item)
                    for _item in obj["accountIdentifications"]
                ]
                if obj.get("accountIdentifications") is not None
                else None,
                "country": obj.get("country"),
            }
        )
        return _obj
