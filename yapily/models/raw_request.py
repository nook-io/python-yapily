import json
import pprint
from datetime import datetime
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class RawRequest(BaseModel):
    """
    RawRequest
    """

    method: StrictStr | None = None
    url: StrictStr | None = None
    request_instant: Annotated[datetime | None, Field(alias="requestInstant")] = None
    headers: dict[str, StrictStr] | None = None
    body: dict[str, Any] | None = None
    body_parameters: Annotated[dict[str, StrictStr] | None, Field(alias="bodyParameters")] = None
    start_time: Annotated[datetime | None, Field(alias="startTime")] = None
    started_at: Annotated[datetime | None, Field(alias="startedAt")] = None
    __properties = ["method", "url", "requestInstant", "headers", "body", "bodyParameters", "startTime", "startedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RawRequest":
        """Create an instance of RawRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "RawRequest":
        """Create an instance of RawRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RawRequest.parse_obj(obj)

        return RawRequest.parse_obj(
            {
                "method": obj.get("method"),
                "url": obj.get("url"),
                "request_instant": obj.get("requestInstant"),
                "headers": obj.get("headers"),
                "body": obj.get("body"),
                "body_parameters": obj.get("bodyParameters"),
                "start_time": obj.get("startTime"),
                "started_at": obj.get("startedAt"),
            }
        )
