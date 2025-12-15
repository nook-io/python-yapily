from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.category_structure import CategoryStructure
from typing import Set
from typing_extensions import Self


class GetWebhookEventsCategories200ResponseData(BaseModel):
    categories: Optional[List[CategoryStructure]] = None
    __properties: ClassVar[List[str]] = ["categories"]
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
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict["categories"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "categories": [
                    CategoryStructure.from_dict(_item) for _item in obj["categories"]
                ]
                if obj.get("categories") is not None
                else None
            }
        )
        return _obj
