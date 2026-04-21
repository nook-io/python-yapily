import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class SchemaXYapilyAnnotations(BaseModel):
    """
    SchemaXYapilyAnnotations
    """

    last_updated_at: Annotated[datetime | None, Field(alias="lastUpdatedAt")] = None
    __properties = ["lastUpdatedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SchemaXYapilyAnnotations":
        """Create an instance of SchemaXYapilyAnnotations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "SchemaXYapilyAnnotations":
        """Create an instance of SchemaXYapilyAnnotations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchemaXYapilyAnnotations.parse_obj(obj)

        return SchemaXYapilyAnnotations.parse_obj({"last_updated_at": obj.get("lastUpdatedAt")})
