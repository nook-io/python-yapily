import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.api_error_response_v2_error import ApiErrorResponseV2Error


class ApiErrorResponseV2(BaseModel):
    """
    API Error Response  # noqa: E501
    """

    error: ApiErrorResponseV2Error | None = None
    __properties = ["error"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiErrorResponseV2":
        """Create an instance of ApiErrorResponseV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiErrorResponseV2":
        """Create an instance of ApiErrorResponseV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorResponseV2.parse_obj(obj)

        return ApiErrorResponseV2.parse_obj(
            {"error": ApiErrorResponseV2Error.from_dict(obj.get("error")) if obj.get("error") is not None else None}
        )
