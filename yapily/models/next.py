import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class Next(BaseModel):
    """
    Next
    """

    var_from: Annotated[datetime | None, Field(alias="from")] = None
    before: datetime | None = None
    limit: StrictInt | None = None
    cursor: StrictStr | None = None
    __properties = ["from", "before", "limit", "cursor"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Next":
        """Create an instance of Next from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Next":
        """Create an instance of Next from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Next.model_validate(obj)

        return Next.model_validate(
            {
                "var_from": obj.get("from"),
                "before": obj.get("before"),
                "limit": obj.get("limit"),
                "cursor": obj.get("cursor"),
            }
        )
