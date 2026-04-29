import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ApplicationResponseListMetaPaginationSelf(BaseModel):
    """
    ApplicationResponseListMetaPaginationSelf
    """

    offset: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None, Field(description="The number of skipped applications.")
    ] = None
    limit: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None,
        Field(description="The maximum number of applications for the current page."),
    ] = None
    sort: Annotated[
        StrictStr | None,
        Field(
            description='The field by which results are sorted by. Default direction is ascending, descending is identified by a "-" prefix.'
        ),
    ] = None
    __properties = ["offset", "limit", "sort"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApplicationResponseListMetaPaginationSelf":
        """Create an instance of ApplicationResponseListMetaPaginationSelf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ApplicationResponseListMetaPaginationSelf":
        """Create an instance of ApplicationResponseListMetaPaginationSelf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationResponseListMetaPaginationSelf.model_validate(obj)

        return ApplicationResponseListMetaPaginationSelf.model_validate(
            {"offset": obj.get("offset"), "limit": obj.get("limit"), "sort": obj.get("sort")}
        )
