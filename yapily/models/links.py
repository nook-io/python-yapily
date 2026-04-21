import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class Links(BaseModel):
    """
    Links
    """

    var_self: Annotated[StrictStr | None, Field(alias="self")] = None
    first: StrictStr | None = None
    last: StrictStr | None = None
    next: StrictStr | None = None
    previous: StrictStr | None = None
    __properties = ["self", "first", "last", "next", "previous"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Links":
        """Create an instance of Links from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Links":
        """Create an instance of Links from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Links.parse_obj(obj)

        return Links.parse_obj(
            {
                "var_self": obj.get("self"),
                "first": obj.get("first"),
                "last": obj.get("last"),
                "next": obj.get("next"),
                "previous": obj.get("previous"),
            }
        )
