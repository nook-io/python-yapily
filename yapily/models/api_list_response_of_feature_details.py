import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.feature_details import FeatureDetails
from yapily.models.filtered_client_payload_list_feature_details import FilteredClientPayloadListFeatureDetails
from yapily.models.raw_response import RawResponse
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_list_meta import ResponseListMeta


class ApiListResponseOfFeatureDetails(BaseModel):
    """
    ApiListResponseOfFeatureDetails
    """

    meta: ResponseListMeta | None = None
    data: list[FeatureDetails] | None = None
    links: dict[str, StrictStr] | None = None
    forwarded_data: Annotated[list[ResponseForwardedData] | None, Field(alias="forwardedData")] = None
    raw: list[RawResponse] | None = None
    paging: FilteredClientPayloadListFeatureDetails | None = None
    tracing_id: Annotated[StrictStr | None, Field(alias="tracingId")] = None
    __properties = ["meta", "data", "links", "forwardedData", "raw", "paging", "tracingId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiListResponseOfFeatureDetails":
        """Create an instance of ApiListResponseOfFeatureDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict["paging"] = self.paging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiListResponseOfFeatureDetails":
        """Create an instance of ApiListResponseOfFeatureDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiListResponseOfFeatureDetails.model_validate(obj)

        return ApiListResponseOfFeatureDetails.model_validate(
            {
                "meta": ResponseListMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
                "data": [FeatureDetails.from_dict(_item) for _item in obj.get("data")]
                if obj.get("data") is not None
                else None,
                "links": obj.get("links"),
                "forwarded_data": [ResponseForwardedData.from_dict(_item) for _item in obj.get("forwardedData")]
                if obj.get("forwardedData") is not None
                else None,
                "raw": [RawResponse.from_dict(_item) for _item in obj.get("raw")]
                if obj.get("raw") is not None
                else None,
                "paging": FilteredClientPayloadListFeatureDetails.from_dict(obj.get("paging"))
                if obj.get("paging") is not None
                else None,
                "tracing_id": obj.get("tracingId"),
            }
        )
