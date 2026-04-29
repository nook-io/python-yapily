import json
import pprint
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.raw_request import RawRequest


class RawResponse(BaseModel):
    """
    Interaction (raw request and response) that occured with the `Institution` in order to fulfil a request.  # noqa: E501
    """

    request: RawRequest | None = None
    duration: StrictStr | None = None
    headers: dict[str, StrictStr] | None = None
    result_code: Annotated[StrictInt | None, Field(alias="resultCode")] = None
    result: dict[str, Any] | None = None
    __properties = ["request", "duration", "headers", "resultCode", "result"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RawResponse":
        """Create an instance of RawResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of request
        if self.request:
            _dict["request"] = self.request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RawResponse":
        """Create an instance of RawResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RawResponse.model_validate(obj)

        return RawResponse.model_validate(
            {
                "request": RawRequest.from_dict(obj.get("request")) if obj.get("request") is not None else None,
                "duration": obj.get("duration"),
                "headers": obj.get("headers"),
                "result_code": obj.get("resultCode"),
                "result": obj.get("result"),
            }
        )
