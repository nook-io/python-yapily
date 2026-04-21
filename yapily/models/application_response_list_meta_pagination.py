import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.application_response_list_meta_pagination_self import ApplicationResponseListMetaPaginationSelf


class ApplicationResponseListMetaPagination(BaseModel):
    """
    ApplicationResponseListMetaPagination
    """

    var_self: Annotated[ApplicationResponseListMetaPaginationSelf | None, Field(alias="self")] = None
    total_count: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None,
        Field(alias="totalCount", description="The total number of applications that match the given filter."),
    ] = None
    __properties = ["self", "totalCount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApplicationResponseListMetaPagination":
        """Create an instance of ApplicationResponseListMetaPagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict["self"] = self.var_self.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApplicationResponseListMetaPagination":
        """Create an instance of ApplicationResponseListMetaPagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationResponseListMetaPagination.parse_obj(obj)

        return ApplicationResponseListMetaPagination.parse_obj(
            {
                "var_self": ApplicationResponseListMetaPaginationSelf.from_dict(obj.get("self"))
                if obj.get("self") is not None
                else None,
                "total_count": obj.get("totalCount"),
            }
        )
