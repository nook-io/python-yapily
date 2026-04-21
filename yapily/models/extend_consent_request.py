import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class ExtendConsentRequest(BaseModel):
    """
    ExtendConsentRequest
    """

    last_confirmed_at: Annotated[
        datetime,
        Field(
            alias="lastConfirmedAt",
            description="__Mandatory__. The time that the user confirmed access to their account information",
        ),
    ]
    __properties = ["lastConfirmedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ExtendConsentRequest":
        """Create an instance of ExtendConsentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ExtendConsentRequest":
        """Create an instance of ExtendConsentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtendConsentRequest.parse_obj(obj)

        return ExtendConsentRequest.parse_obj({"last_confirmed_at": obj.get("lastConfirmedAt")})
