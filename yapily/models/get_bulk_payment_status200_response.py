import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.get_bulk_payment_status200_response_data import GetBulkPaymentStatus200ResponseData
from yapily.models.get_bulk_payment_status200_response_meta import GetBulkPaymentStatus200ResponseMeta


class GetBulkPaymentStatus200Response(BaseModel):
    """
    GetBulkPaymentStatus200Response
    """

    meta: GetBulkPaymentStatus200ResponseMeta | None = None
    data: GetBulkPaymentStatus200ResponseData | None = None
    __properties = ["meta", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetBulkPaymentStatus200Response":
        """Create an instance of GetBulkPaymentStatus200Response from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetBulkPaymentStatus200Response":
        """Create an instance of GetBulkPaymentStatus200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetBulkPaymentStatus200Response.model_validate(obj)

        return GetBulkPaymentStatus200Response.model_validate(
            {
                "meta": GetBulkPaymentStatus200ResponseMeta.from_dict(obj.get("meta"))
                if obj.get("meta") is not None
                else None,
                "data": GetBulkPaymentStatus200ResponseData.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
            }
        )
