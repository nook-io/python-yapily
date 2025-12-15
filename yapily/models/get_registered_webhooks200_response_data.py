from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.registered_webhook_with_status import RegisteredWebhookWithStatus
from typing import Set
from typing_extensions import Self


class GetRegisteredWebhooks200ResponseData(BaseModel):
    active: Optional[List[RegisteredWebhookWithStatus]] = None
    __properties: ClassVar[List[str]] = ["active"]
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
        if self.active:
            for _item_active in self.active:
                if _item_active:
                    _items.append(_item_active.to_dict())
            _dict["active"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "active": [
                    RegisteredWebhookWithStatus.from_dict(_item)
                    for _item in obj["active"]
                ]
                if obj.get("active") is not None
                else None
            }
        )
        return _obj
