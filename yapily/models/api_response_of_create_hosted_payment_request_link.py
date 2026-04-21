import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.hosted_payment_request_response import HostedPaymentRequestResponse
from yapily.models.response_meta import ResponseMeta


class ApiResponseOfCreateHostedPaymentRequestLink(BaseModel):
    """
    ApiResponseOfCreateHostedPaymentRequestLink
    """

    meta: ResponseMeta | None = None
    data: HostedPaymentRequestResponse | None = None
    __properties = ["meta", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiResponseOfCreateHostedPaymentRequestLink":
        """Create an instance of ApiResponseOfCreateHostedPaymentRequestLink from a JSON string"""
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
    def from_dict(cls, obj: dict) -> "ApiResponseOfCreateHostedPaymentRequestLink":
        """Create an instance of ApiResponseOfCreateHostedPaymentRequestLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResponseOfCreateHostedPaymentRequestLink.parse_obj(obj)

        return ApiResponseOfCreateHostedPaymentRequestLink.parse_obj(
            {
                "meta": ResponseMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
                "data": HostedPaymentRequestResponse.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
            }
        )
