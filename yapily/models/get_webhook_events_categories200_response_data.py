import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.category_structure import CategoryStructure


class GetWebhookEventsCategories200ResponseData(BaseModel):
    """
    GetWebhookEventsCategories200ResponseData
    """

    categories: Annotated[list[CategoryStructure], Field()] | None = None
    __properties = ["categories"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetWebhookEventsCategories200ResponseData":
        """Create an instance of GetWebhookEventsCategories200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict["categories"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetWebhookEventsCategories200ResponseData":
        """Create an instance of GetWebhookEventsCategories200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetWebhookEventsCategories200ResponseData.model_validate(obj)

        return GetWebhookEventsCategories200ResponseData.model_validate(
            {
                "categories": [CategoryStructure.from_dict(_item) for _item in obj.get("categories")]
                if obj.get("categories") is not None
                else None
            }
        )
