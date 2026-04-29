import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.application_response_list_meta_pagination import ApplicationResponseListMetaPagination


class ApplicationResponseListMeta(BaseModel):
    """
    ApplicationResponseListMeta
    """

    tracing_id: Annotated[StrictStr | None, Field(alias="tracingId")] = None
    count: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None,
        Field(description="The number of applications in the current page."),
    ] = None
    pagination: ApplicationResponseListMetaPagination | None = None
    __properties = ["tracingId", "count", "pagination"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApplicationResponseListMeta":
        """Create an instance of ApplicationResponseListMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApplicationResponseListMeta":
        """Create an instance of ApplicationResponseListMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationResponseListMeta.model_validate(obj)

        return ApplicationResponseListMeta.model_validate(
            {
                "tracing_id": obj.get("tracingId"),
                "count": obj.get("count"),
                "pagination": ApplicationResponseListMetaPagination.from_dict(obj.get("pagination"))
                if obj.get("pagination") is not None
                else None,
            }
        )
