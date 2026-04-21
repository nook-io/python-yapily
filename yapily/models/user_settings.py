import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class UserSettings(BaseModel):
    """
    Specifies the language and location preferences of the user.  # noqa: E501
    """

    language: Annotated[
        StrictStr | None,
        Field(description="2 letter ISO Language code which denotes the language preference for the `User`."),
    ] = None
    location: Annotated[
        StrictStr | None,
        Field(description="2 letter ISO Country code which denotes the location preference for the `User`."),
    ] = None
    __properties = ["language", "location"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "UserSettings":
        """Create an instance of UserSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "UserSettings":
        """Create an instance of UserSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserSettings.parse_obj(obj)

        return UserSettings.parse_obj({"language": obj.get("language"), "location": obj.get("location")})
