from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_identification import AccountIdentification
from typing import Set
from typing_extensions import Self


class AccountInfo(BaseModel):
    account_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Unique identifier of the account.",
        alias="accountId",
    )
    account_identification: AccountIdentification = Field(alias="accountIdentification")
    __properties: ClassVar[List[str]] = ["accountId", "accountIdentification"]
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
        if self.account_identification:
            _dict["accountIdentification"] = self.account_identification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "accountId": obj.get("accountId"),
                "accountIdentification": AccountIdentification.from_dict(
                    obj["accountIdentification"]
                )
                if obj.get("accountIdentification") is not None
                else None,
            }
        )
        return _obj
