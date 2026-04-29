import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class Subcategory(BaseModel):
    """
    Subcategory
    """

    id: StrictStr | None = None
    label: StrictStr | None = None
    __properties = ["id", "label"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Subcategory":
        """Create an instance of Subcategory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Subcategory":
        """Create an instance of Subcategory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Subcategory.model_validate(obj)

        return Subcategory.model_validate({"id": obj.get("id"), "label": obj.get("label")})
