import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.validation_error import ValidationError


class ValidationErrorResponse(BaseModel):
    """
    ValidationErrorResponse
    """

    errors: Annotated[list[ValidationError], Field()] | None = None
    __properties = ["errors"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ValidationErrorResponse":
        """Create an instance of ValidationErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["errors"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ValidationErrorResponse":
        """Create an instance of ValidationErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationErrorResponse.model_validate(obj)

        return ValidationErrorResponse.model_validate(
            {
                "errors": [ValidationError.from_dict(_item) for _item in obj.get("errors")]
                if obj.get("errors") is not None
                else None
            }
        )
