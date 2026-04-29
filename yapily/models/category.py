import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.subcategory import Subcategory


class Category(BaseModel):
    """
    Income and Expense `Category` in which the transaction resides.  # noqa: E501
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier of the category")] = None
    label: Annotated[StrictStr | None, Field(description="Descriptive identifier of the category.")] = None
    country: Annotated[
        StrictStr | None,
        Field(
            description="The country code of where the category transaction took place, denoted as a 3-digit character code - ISO 3166."
        ),
    ] = None
    subcategories: Annotated[list[Subcategory], Field()] | None = None
    __properties = ["id", "label", "country", "subcategories"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Category":
        """Create an instance of Category from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in subcategories (list)
        _items = []
        if self.subcategories:
            for _item in self.subcategories:
                if _item:
                    _items.append(_item.to_dict())
            _dict["subcategories"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "Category":
        """Create an instance of Category from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Category.model_validate(obj)

        return Category.model_validate(
            {
                "id": obj.get("id"),
                "label": obj.get("label"),
                "country": obj.get("country"),
                "subcategories": [Subcategory.from_dict(_item) for _item in obj.get("subcategories")]
                if obj.get("subcategories") is not None
                else None,
            }
        )
