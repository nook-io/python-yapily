import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class AccountStatement(BaseModel):
    """
    Statement information belonging to the account.  # noqa: E501
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier for the statement.")] = None
    start_date_time: Annotated[
        datetime | None, Field(alias="startDateTime", description="Date and time of when the statement period starts.")
    ] = None
    end_date_time: Annotated[
        datetime | None, Field(alias="endDateTime", description="Date and time of when the statement period ends.")
    ] = None
    creation_date_time: Annotated[
        datetime | None, Field(alias="creationDateTime", description="Date and time of when the statement was created.")
    ] = None
    __properties = ["id", "startDateTime", "endDateTime", "creationDateTime"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AccountStatement":
        """Create an instance of AccountStatement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "AccountStatement":
        """Create an instance of AccountStatement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountStatement.parse_obj(obj)

        return AccountStatement.parse_obj(
            {
                "id": obj.get("id"),
                "start_date_time": obj.get("startDateTime"),
                "end_date_time": obj.get("endDateTime"),
                "creation_date_time": obj.get("creationDateTime"),
            }
        )
