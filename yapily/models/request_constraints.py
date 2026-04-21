import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.model_schema import ModelSchema


class RequestConstraints(BaseModel):
    """
    Object defining the constraints rules applicable for a given requests.  # noqa: E501
    """

    headers: ModelSchema | None = None
    body: Annotated[ModelSchema, Field()]
    __properties = ["headers", "body"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RequestConstraints":
        """Create an instance of RequestConstraints from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of headers
        if self.headers:
            _dict["headers"] = self.headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict["body"] = self.body.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RequestConstraints":
        """Create an instance of RequestConstraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestConstraints.parse_obj(obj)

        return RequestConstraints.parse_obj(
            {
                "headers": ModelSchema.from_dict(obj.get("headers")) if obj.get("headers") is not None else None,
                "body": ModelSchema.from_dict(obj.get("body")) if obj.get("body") is not None else None,
            }
        )
