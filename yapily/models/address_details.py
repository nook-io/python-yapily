import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class AddressDetails(BaseModel):
    """
    AddressDetails
    """

    address_line: Annotated[
        StrictStr | None,
        Field(alias="addressLine", description="Information, in free format text, that identifies a specific address."),
    ] = None
    __properties = ["addressLine"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AddressDetails":
        """Create an instance of AddressDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "AddressDetails":
        """Create an instance of AddressDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressDetails.parse_obj(obj)

        return AddressDetails.parse_obj({"address_line": obj.get("addressLine")})
