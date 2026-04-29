import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class OneTimeTokenRequest(BaseModel):
    """
    The request body containing the `OneTimeTokenRequest` json payload  # noqa: E501
    """

    one_time_token: Annotated[
        StrictStr,
        Field(alias="oneTimeToken", description="__Mandatory__. The one time token to exchange for a consent token."),
    ]
    __properties = ["oneTimeToken"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "OneTimeTokenRequest":
        """Create an instance of OneTimeTokenRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "OneTimeTokenRequest":
        """Create an instance of OneTimeTokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OneTimeTokenRequest.model_validate(obj)

        return OneTimeTokenRequest.model_validate({"one_time_token": obj.get("oneTimeToken")})
