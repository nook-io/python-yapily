# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.payment_type_of_constraints import PaymentTypeOfConstraints
from yapily.models.request_constraints import RequestConstraints

class PaymentConstraintsResponse(BaseModel):
    """
    PaymentConstraintsResponse
    """
    institution_id: StrictStr = Field(..., alias="institutionId", description="The id to represent the `Institution`.")
    institution_country_code: Optional[StrictStr] = Field(None, alias="institutionCountryCode", description="2 letter ISO Country code of the `Institution`.")
    endpoint_path: Optional[StrictStr] = Field(None, alias="endpointPath", description="Define the applicable API end point.")
    endpoint_method: Optional[StrictStr] = Field(None, alias="endpointMethod", description="Https Method for the endpoint.")
    payment_type: PaymentTypeOfConstraints = Field(..., alias="paymentType")
    request: RequestConstraints = Field(...)
    __properties = ["institutionId", "institutionCountryCode", "endpointPath", "endpointMethod", "paymentType", "request"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PaymentConstraintsResponse:
        """Create an instance of PaymentConstraintsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of request
        if self.request:
            _dict['request'] = self.request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentConstraintsResponse:
        """Create an instance of PaymentConstraintsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentConstraintsResponse.parse_obj(obj)

        _obj = PaymentConstraintsResponse.parse_obj({
            "institution_id": obj.get("institutionId"),
            "institution_country_code": obj.get("institutionCountryCode"),
            "endpoint_path": obj.get("endpointPath"),
            "endpoint_method": obj.get("endpointMethod"),
            "payment_type": obj.get("paymentType"),
            "request": RequestConstraints.from_dict(obj.get("request")) if obj.get("request") is not None else None
        })
        return _obj


