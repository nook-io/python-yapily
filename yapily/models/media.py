import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class Media(BaseModel):
    """
    Details of the media held for the `Institution`  # noqa: E501
    """

    source: Annotated[
        StrictStr | None, Field(description="__Mandatory__. URL from where the media can be retrieved.")
    ] = None
    type: Annotated[StrictStr | None, Field(description="__Mandatory__. The type of media e.g. (logo, icon).")] = None
    __properties = ["source", "type"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Media":
        """Create an instance of Media from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Media":
        """Create an instance of Media from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Media.parse_obj(obj)

        return Media.parse_obj({"source": obj.get("source"), "type": obj.get("type")})
