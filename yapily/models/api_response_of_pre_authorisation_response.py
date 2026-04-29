import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.pre_authorisation_response import PreAuthorisationResponse
from yapily.models.raw_response import RawResponse
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_meta import ResponseMeta


class ApiResponseOfPreAuthorisationResponse(BaseModel):
    """
    ApiResponseOfPreAuthorisationResponse
    """

    meta: ResponseMeta | None = None
    data: PreAuthorisationResponse | None = None
    links: dict[str, StrictStr] | None = None
    forwarded_data: Annotated[list[ResponseForwardedData] | None, Field(alias="forwardedData")] = None
    raw: Annotated[list[RawResponse], Field()] | None = None
    tracing_id: Annotated[StrictStr | None, Field(alias="tracingId")] = None
    __properties = ["meta", "data", "links", "forwardedData", "raw", "tracingId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiResponseOfPreAuthorisationResponse":
        """Create an instance of ApiResponseOfPreAuthorisationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in forwarded_data (list)
        _items = []
        if self.forwarded_data:
            for _item in self.forwarded_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict["forwardedData"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item in self.raw:
                if _item:
                    _items.append(_item.to_dict())
            _dict["raw"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiResponseOfPreAuthorisationResponse":
        """Create an instance of ApiResponseOfPreAuthorisationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResponseOfPreAuthorisationResponse.model_validate(obj)

        return ApiResponseOfPreAuthorisationResponse.model_validate(
            {
                "meta": ResponseMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
                "data": PreAuthorisationResponse.from_dict(obj.get("data")) if obj.get("data") is not None else None,
                "links": obj.get("links"),
                "forwarded_data": [ResponseForwardedData.from_dict(_item) for _item in obj.get("forwardedData")]
                if obj.get("forwardedData") is not None
                else None,
                "raw": [RawResponse.from_dict(_item) for _item in obj.get("raw")]
                if obj.get("raw") is not None
                else None,
                "tracing_id": obj.get("tracingId"),
            }
        )
