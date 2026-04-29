import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.application_response import ApplicationResponse
from yapily.models.application_response_list_meta import ApplicationResponseListMeta


class ApiListOfApplicationResponse(BaseModel):
    """
    ApiListOfApplicationResponse
    """

    meta: ApplicationResponseListMeta | None = None
    data: list[ApplicationResponse] | None = None
    __properties = ["meta", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiListOfApplicationResponse":
        """Create an instance of ApiListOfApplicationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["data"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiListOfApplicationResponse":
        """Create an instance of ApiListOfApplicationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiListOfApplicationResponse.model_validate(obj)

        return ApiListOfApplicationResponse.model_validate(
            {
                "meta": ApplicationResponseListMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
                "data": [ApplicationResponse.from_dict(_item) for _item in obj.get("data")]
                if obj.get("data") is not None
                else None,
            }
        )
