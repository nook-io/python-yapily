import json
import pprint
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.feature_details import FeatureDetails
from yapily.models.filter_and_sort import FilterAndSort


class FilteredClientPayloadListFeatureDetails(BaseModel):
    """
    FilteredClientPayloadListFeatureDetails
    """

    api_call: Annotated[dict[str, Any] | None, Field(alias="apiCall")] = None
    data: Annotated[list[FeatureDetails], Field()] | None = None
    next_cursor_hash: Annotated[StrictStr | None, Field(alias="nextCursorHash")] = None
    next_link: Annotated[StrictStr | None, Field(alias="nextLink")] = None
    paging_map: Annotated[dict[str, FilterAndSort] | None, Field(alias="pagingMap")] = None
    total_count: Annotated[StrictInt | None, Field(alias="totalCount")] = None
    __properties = ["apiCall", "data", "nextCursorHash", "nextLink", "pagingMap", "totalCount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FilteredClientPayloadListFeatureDetails":
        """Create an instance of FilteredClientPayloadListFeatureDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data"] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in paging_map (dict)
        _field_dict = {}
        if self.paging_map:
            for _key in self.paging_map:
                if self.paging_map[_key]:
                    _field_dict[_key] = self.paging_map[_key].to_dict()
            _dict["pagingMap"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "FilteredClientPayloadListFeatureDetails":
        """Create an instance of FilteredClientPayloadListFeatureDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilteredClientPayloadListFeatureDetails.model_validate(obj)

        return FilteredClientPayloadListFeatureDetails.model_validate(
            {
                "api_call": obj.get("apiCall"),
                "data": [FeatureDetails.from_dict(_item) for _item in obj.get("data")]
                if obj.get("data") is not None
                else None,
                "next_cursor_hash": obj.get("nextCursorHash"),
                "next_link": obj.get("nextLink"),
                "paging_map": {_k: FilterAndSort.from_dict(_v) for _k, _v in obj.get("pagingMap").items()}
                if obj.get("pagingMap") is not None
                else None,
                "total_count": obj.get("totalCount"),
            }
        )
