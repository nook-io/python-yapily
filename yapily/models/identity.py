from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.identity_address import IdentityAddress
from typing import Set
from typing_extensions import Self


class Identity(BaseModel):
    id: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    gender: Optional[StrictStr] = None
    birthdate: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    addresses: Optional[List[IdentityAddress]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "firstName",
        "lastName",
        "fullName",
        "gender",
        "birthdate",
        "email",
        "phone",
        "addresses",
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
        if self.addresses:
            for _item_addresses in self.addresses:
                if _item_addresses:
                    _items.append(_item_addresses.to_dict())
            _dict["addresses"] = _items
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
                "firstName": obj.get("firstName"),
                "lastName": obj.get("lastName"),
                "fullName": obj.get("fullName"),
                "gender": obj.get("gender"),
                "birthdate": obj.get("birthdate"),
                "email": obj.get("email"),
                "phone": obj.get("phone"),
                "addresses": [
                    IdentityAddress.from_dict(_item) for _item in obj["addresses"]
                ]
                if obj.get("addresses") is not None
                else None,
            }
        )
        return _obj
