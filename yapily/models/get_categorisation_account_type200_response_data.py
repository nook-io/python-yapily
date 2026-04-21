import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class GetCategorisationAccountType200ResponseData(BaseModel):
    """
    GetCategorisationAccountType200ResponseData
    """

    incoming: Annotated[list[StrictStr], Field()] | None = None
    outgoing: Annotated[list[StrictStr], Field()] | None = None
    __properties = ["incoming", "outgoing"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetCategorisationAccountType200ResponseData":
        """Create an instance of GetCategorisationAccountType200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "GetCategorisationAccountType200ResponseData":
        """Create an instance of GetCategorisationAccountType200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetCategorisationAccountType200ResponseData.parse_obj(obj)

        return GetCategorisationAccountType200ResponseData.parse_obj(
            {"incoming": obj.get("incoming"), "outgoing": obj.get("outgoing")}
        )
