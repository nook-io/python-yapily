import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ApiErrorResponseV2ErrorIssuesInner(BaseModel):
    """
    Detailed information regarding the issue that was experienced during processing of the request  # noqa: E501
    """

    type: Annotated[StrictStr | None, Field(description="Category of the issue")] = None
    code: Annotated[
        StrictStr,
        Field(
            description="5 digit Error Code that uniquely identifies the type of issue, for full list of error codes pelase check our documentation"
        ),
    ]
    message: Annotated[StrictStr, Field(description="Human readable description of the issue that was experienced")]
    __properties = ["type", "code", "message"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiErrorResponseV2ErrorIssuesInner":
        """Create an instance of ApiErrorResponseV2ErrorIssuesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiErrorResponseV2ErrorIssuesInner":
        """Create an instance of ApiErrorResponseV2ErrorIssuesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorResponseV2ErrorIssuesInner.model_validate(obj)

        return ApiErrorResponseV2ErrorIssuesInner.model_validate(
            {"type": obj.get("type"), "code": obj.get("code"), "message": obj.get("message")}
        )
