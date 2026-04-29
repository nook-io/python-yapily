import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ApiListResponseOfRealTimeTransactionLinks(BaseModel):
    """
    ApiListResponseOfRealTimeTransactionLinks
    """

    first: Annotated[StrictStr | None, Field(description="A cursor or link to the first page in the data set.")] = None
    prev: Annotated[StrictStr | None, Field(description="A cursor or link to the previous page in the data set.")] = (
        None
    )
    var_self: Annotated[
        StrictStr | None, Field(alias="self", description="A cursor or link to the current page in the data set.")
    ] = None
    next: Annotated[StrictStr | None, Field(description="A cursor or link to the next page in the data set.")] = None
    last: Annotated[StrictStr | None, Field(description="A cursor or link to the last page in the data set.")] = None
    __properties = ["first", "prev", "self", "next", "last"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiListResponseOfRealTimeTransactionLinks":
        """Create an instance of ApiListResponseOfRealTimeTransactionLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiListResponseOfRealTimeTransactionLinks":
        """Create an instance of ApiListResponseOfRealTimeTransactionLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiListResponseOfRealTimeTransactionLinks.model_validate(obj)

        return ApiListResponseOfRealTimeTransactionLinks.model_validate(
            {
                "first": obj.get("first"),
                "prev": obj.get("prev"),
                "var_self": obj.get("self"),
                "next": obj.get("next"),
                "last": obj.get("last"),
            }
        )
