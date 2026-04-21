import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class AccountName(BaseModel):
    """
    AccountName
    """

    name: Annotated[
        StrictStr | None, Field(description="The bank account holder's name given by the account owner.")
    ] = None
    __properties = ["name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AccountName":
        """Create an instance of AccountName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "AccountName":
        """Create an instance of AccountName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountName.parse_obj(obj)

        return AccountName.parse_obj({"name": obj.get("name")})
