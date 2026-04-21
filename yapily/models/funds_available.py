import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool


class FundsAvailable(BaseModel):
    """
    FundsAvailable
    """

    funds_available: Annotated[
        StrictBool,
        Field(alias="fundsAvailable", description="__Mandatory__. Indicates whether funds are available or not."),
    ]
    funds_available_at: Annotated[
        datetime,
        Field(
            alias="fundsAvailableAt", description="__Mandatory__. Date and Time when the funds availability is checked."
        ),
    ]
    __properties = ["fundsAvailable", "fundsAvailableAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FundsAvailable":
        """Create an instance of FundsAvailable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "FundsAvailable":
        """Create an instance of FundsAvailable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FundsAvailable.parse_obj(obj)

        return FundsAvailable.parse_obj(
            {"funds_available": obj.get("fundsAvailable"), "funds_available_at": obj.get("fundsAvailableAt")}
        )
