from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class UserCredentials(BaseModel):
    id: StrictStr = Field(
        description="__Mandatory__. The login id for the user for a particular `Institution`."
    )
    corporate_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. The corporate login for the user for a particular corporate `Institution`.",
        alias="corporateId",
    )
    password: StrictStr = Field(
        description="__Mandatory__. The password of the user to login to a particular `Institution`."
    )
    __properties: ClassVar[List[str]] = ["id", "corporateId", "password"]
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
                "corporateId": obj.get("corporateId"),
                "password": obj.get("password"),
            }
        )
        return _obj
