import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.hosted_vrp_payment_response import HostedVRPPaymentResponse
from yapily.models.response_meta import ResponseMeta


class ApiResponseOfCreateHostedVRPPaymentRequest(BaseModel):
    """
    ApiResponseOfCreateHostedVRPPaymentRequest
    """

    meta: ResponseMeta | None = None
    data: HostedVRPPaymentResponse | None = None
    tracing_id: Annotated[StrictStr | None, Field(alias="tracingId")] = None
    __properties = ["meta", "data", "tracingId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiResponseOfCreateHostedVRPPaymentRequest":
        """Create an instance of ApiResponseOfCreateHostedVRPPaymentRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> "ApiResponseOfCreateHostedVRPPaymentRequest":
        """Create an instance of ApiResponseOfCreateHostedVRPPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResponseOfCreateHostedVRPPaymentRequest.model_validate(obj)

        return ApiResponseOfCreateHostedVRPPaymentRequest.model_validate(
            {
                "meta": ResponseMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
                "data": HostedVRPPaymentResponse.from_dict(obj.get("data")) if obj.get("data") is not None else None,
                "tracing_id": obj.get("tracingId"),
            }
        )
