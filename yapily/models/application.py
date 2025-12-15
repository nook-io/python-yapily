from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution import Institution
from yapily.models.media import Media
from typing import Set
from typing_extensions import Self


class Application(BaseModel):
    uuid: Optional[StrictStr] = Field(
        default=None,
        description="Unique identification for the `Application` as assigned by Yapily.",
    )
    name: Optional[StrictStr] = Field(
        default=None, description="The individual name of the `Application`."
    )
    active: Optional[StrictBool] = Field(
        default=None, description="States whether an `Application` is active."
    )
    auth_callbacks: Optional[List[StrictStr]] = Field(
        default=None, alias="authCallbacks"
    )
    institutions: Optional[List[Institution]] = None
    media: Optional[List[Media]] = None
    created: Optional[datetime] = Field(
        default=None, description="Date and time of when the application was created."
    )
    updated: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the application was last updated.",
    )
    __properties: ClassVar[List[str]] = [
        "uuid",
        "name",
        "active",
        "authCallbacks",
        "institutions",
        "media",
        "created",
        "updated",
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
        if self.institutions:
            for _item_institutions in self.institutions:
                if _item_institutions:
                    _items.append(_item_institutions.to_dict())
            _dict["institutions"] = _items
        _items = []
        if self.media:
            for _item_media in self.media:
                if _item_media:
                    _items.append(_item_media.to_dict())
            _dict["media"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "uuid": obj.get("uuid"),
                "name": obj.get("name"),
                "active": obj.get("active"),
                "authCallbacks": obj.get("authCallbacks"),
                "institutions": [
                    Institution.from_dict(_item) for _item in obj["institutions"]
                ]
                if obj.get("institutions") is not None
                else None,
                "media": [Media.from_dict(_item) for _item in obj["media"]]
                if obj.get("media") is not None
                else None,
                "created": obj.get("created"),
                "updated": obj.get("updated"),
            }
        )
        return _obj
