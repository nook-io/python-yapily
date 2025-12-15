from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_statement import AccountStatement
from yapily.models.filter_and_sort import FilterAndSort
from typing import Set
from typing_extensions import Self


class FilteredClientPayloadListAccountStatement(BaseModel):
    api_call: Optional[Dict[str, Any]] = Field(default=None, alias="apiCall")
    data: Optional[List[AccountStatement]] = None
    next_cursor_hash: Optional[StrictStr] = Field(default=None, alias="nextCursorHash")
    next_link: Optional[StrictStr] = Field(default=None, alias="nextLink")
    paging_map: Optional[Dict[str, FilterAndSort]] = Field(
        default=None, alias="pagingMap"
    )
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    __properties: ClassVar[List[str]] = [
        "apiCall",
        "data",
        "nextCursorHash",
        "nextLink",
        "pagingMap",
        "totalCount",
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
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict["data"] = _items
        _field_dict = {}
        if self.paging_map:
            for _key_paging_map in self.paging_map:
                if self.paging_map[_key_paging_map]:
                    _field_dict[_key_paging_map] = self.paging_map[
                        _key_paging_map
                    ].to_dict()
            _dict["pagingMap"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "apiCall": obj.get("apiCall"),
                "data": [AccountStatement.from_dict(_item) for _item in obj["data"]]
                if obj.get("data") is not None
                else None,
                "nextCursorHash": obj.get("nextCursorHash"),
                "nextLink": obj.get("nextLink"),
                "pagingMap": dict(
                    (_k, FilterAndSort.from_dict(_v))
                    for _k, _v in obj["pagingMap"].items()
                )
                if obj.get("pagingMap") is not None
                else None,
                "totalCount": obj.get("totalCount"),
            }
        )
        return _obj
