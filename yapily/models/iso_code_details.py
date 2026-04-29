import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class IsoCodeDetails(BaseModel):
    """
    __Mandatory__. Details the identification of the ISO code.  # noqa: E501
    """

    code: Annotated[StrictStr | None, Field(description="__Mandatory__. Unique identifier of the ISO code.")] = (
        "UNKNOWN"
    )
    name: Annotated[StrictStr | None, Field(description="__Mandatory__. Name of the ISO Code.")] = "UNKNOWN"
    __properties = ["code", "name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "IsoCodeDetails":
        """Create an instance of IsoCodeDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "IsoCodeDetails":
        """Create an instance of IsoCodeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IsoCodeDetails.model_validate(obj)

        return IsoCodeDetails.model_validate(
            {
                "code": obj.get("code") if obj.get("code") is not None else "UNKNOWN",
                "name": obj.get("name") if obj.get("name") is not None else "UNKNOWN",
            }
        )
