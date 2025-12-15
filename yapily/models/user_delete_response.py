from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.consent_delete_response import ConsentDeleteResponse
from yapily.models.delete_status_enum import DeleteStatusEnum
from typing import Set
from typing_extensions import Self


class UserDeleteResponse(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the user."
    )
    delete_status: Optional[DeleteStatusEnum] = Field(
        default=None, alias="deleteStatus"
    )
    creation_date: Optional[datetime] = Field(
        default=None,
        description="Date and time that the user was created.",
        alias="creationDate",
    )
    user_consents: Optional[List[ConsentDeleteResponse]] = Field(
        default=None, alias="userConsents"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "deleteStatus",
        "creationDate",
        "userConsents",
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
        if self.user_consents:
            for _item_user_consents in self.user_consents:
                if _item_user_consents:
                    _items.append(_item_user_consents.to_dict())
            _dict["userConsents"] = _items
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
                "deleteStatus": obj.get("deleteStatus"),
                "creationDate": obj.get("creationDate"),
                "userConsents": [
                    ConsentDeleteResponse.from_dict(_item)
                    for _item in obj["userConsents"]
                ]
                if obj.get("userConsents") is not None
                else None,
            }
        )
        return _obj
