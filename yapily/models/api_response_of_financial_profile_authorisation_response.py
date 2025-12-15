from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.profile_consent import ProfileConsent
from yapily.models.response_meta import ResponseMeta
from typing import Set
from typing_extensions import Self


class ApiResponseOfFinancialProfileAuthorisationResponse(BaseModel):
    meta: Optional[ResponseMeta] = None
    data: Optional[List[ProfileConsent]] = None
    links: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["meta", "data", "links"]
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
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict["data"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "meta": ResponseMeta.from_dict(obj["meta"])
                if obj.get("meta") is not None
                else None,
                "data": [ProfileConsent.from_dict(_item) for _item in obj["data"]]
                if obj.get("data") is not None
                else None,
                "links": obj.get("links"),
            }
        )
        return _obj
