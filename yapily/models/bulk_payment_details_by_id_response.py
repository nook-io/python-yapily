import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.bulk_payment_details_by_id_response_data import BulkPaymentDetailsByIdResponseData
from yapily.models.get_bulk_payment_status200_response_meta import GetBulkPaymentStatus200ResponseMeta


class BulkPaymentDetailsByIdResponse(BaseModel):
    """
    BulkPaymentDetailsByIdResponse
    """

    meta: GetBulkPaymentStatus200ResponseMeta | None = None
    data: BulkPaymentDetailsByIdResponseData | None = None
    __properties = ["meta", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "BulkPaymentDetailsByIdResponse":
        """Create an instance of BulkPaymentDetailsByIdResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "BulkPaymentDetailsByIdResponse":
        """Create an instance of BulkPaymentDetailsByIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BulkPaymentDetailsByIdResponse.parse_obj(obj)

        return BulkPaymentDetailsByIdResponse.parse_obj(
            {
                "meta": GetBulkPaymentStatus200ResponseMeta.from_dict(obj.get("meta"))
                if obj.get("meta") is not None
                else None,
                "data": BulkPaymentDetailsByIdResponseData.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
            }
        )
