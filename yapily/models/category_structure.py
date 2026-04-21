import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class CategoryStructure(BaseModel):
    """
    CategoryStructure
    """

    name: Annotated[StrictStr | None, Field(description="webhook event category name")] = None
    description: Annotated[StrictStr | None, Field(description="description of the webhook event category")] = None
    __properties = ["name", "description"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CategoryStructure":
        """Create an instance of CategoryStructure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "CategoryStructure":
        """Create an instance of CategoryStructure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CategoryStructure.parse_obj(obj)

        return CategoryStructure.parse_obj({"name": obj.get("name"), "description": obj.get("description")})
