import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ConsentAuthCodeRequest(BaseModel):
    """
    The request body containing the `ConsentAuthCodeRequest` json payload  # noqa: E501
    """

    auth_code: Annotated[StrictStr, Field(alias="authCode", description="__Mandatory__. The authorisation code")]
    auth_state: Annotated[StrictStr, Field(alias="authState", description="__Mandatory__. The authorisation state")]
    __properties = ["authCode", "authState"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ConsentAuthCodeRequest":
        """Create an instance of ConsentAuthCodeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ConsentAuthCodeRequest":
        """Create an instance of ConsentAuthCodeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConsentAuthCodeRequest.model_validate(obj)

        return ConsentAuthCodeRequest.model_validate({"auth_code": obj.get("authCode"), "auth_state": obj.get("authState")})
