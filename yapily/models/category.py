from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.subcategory import Subcategory
from typing import Set
from typing_extensions import Self


class Category(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the category"
    )
    label: Optional[StrictStr] = Field(
        default=None, description="Descriptive identifier of the category."
    )
    country: Optional[StrictStr] = Field(
        default=None,
        description="The country code of where the category transaction took place, denoted as a 3-digit character code - ISO 3166.",
    )
    subcategories: Optional[List[Subcategory]] = None
    __properties: ClassVar[List[str]] = ["id", "label", "country", "subcategories"]
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
        if self.subcategories:
            for _item_subcategories in self.subcategories:
                if _item_subcategories:
                    _items.append(_item_subcategories.to_dict())
            _dict["subcategories"] = _items
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
                "label": obj.get("label"),
                "country": obj.get("country"),
                "subcategories": [
                    Subcategory.from_dict(_item) for _item in obj["subcategories"]
                ]
                if obj.get("subcategories") is not None
                else None,
            }
        )
        return _obj
