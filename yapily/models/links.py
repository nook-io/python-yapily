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
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Links":
        """Create an instance of Links from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Links":
        """Create an instance of Links from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Links.model_validate(obj)

        return Links.model_validate(
            {
                "var_self": obj.get("self"),
                "first": obj.get("first"),
                "last": obj.get("last"),
                "next": obj.get("next"),
                "previous": obj.get("previous"),
            }
        )
