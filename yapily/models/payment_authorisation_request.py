# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from yapily.models.payment_request import PaymentRequest
from yapily.models.redirect_request import RedirectRequest


class PaymentAuthorisationRequest(BaseModel):
    """
    The request body containing an `PaymentAuthorisationRequest` json payload  # noqa: E501
    """

    user_uuid: Optional[StrictStr] = Field(default=None, alias="userUuid")
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        alias="applicationUserId",
        description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
    )
    forward_parameters: Optional[conlist(StrictStr)] = Field(
        default=None,
        alias="forwardParameters",
        description="Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect.",
    )
    institution_id: StrictStr = Field(
        default=...,
        alias="institutionId",
        description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.",
    )
    callback: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The URL to redirect the user to after the user complete the authorisation at the `Institution`.",
    )
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(
        default=None,
        alias="oneTimeToken",
        description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.",
    )
    payment_request: PaymentRequest = Field(default=..., alias="paymentRequest")
    __properties = [
        "userUuid",
        "applicationUserId",
        "forwardParameters",
        "institutionId",
        "callback",
        "redirect",
        "oneTimeToken",
        "paymentRequest",
    ]

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
    def from_json(cls, json_str: str) -> PaymentAuthorisationRequest:
        """Create an instance of PaymentAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of redirect
        if self.redirect:
            _dict["redirect"] = self.redirect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_request
        if self.payment_request:
            _dict["paymentRequest"] = self.payment_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentAuthorisationRequest:
        """Create an instance of PaymentAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentAuthorisationRequest.parse_obj(obj)

        _obj = PaymentAuthorisationRequest.parse_obj(
            {
                "user_uuid": obj.get("userUuid"),
                "application_user_id": obj.get("applicationUserId"),
                "forward_parameters": obj.get("forwardParameters"),
                "institution_id": obj.get("institutionId"),
                "callback": obj.get("callback"),
                "redirect": RedirectRequest.from_dict(obj.get("redirect"))
                if obj.get("redirect") is not None
                else None,
                "one_time_token": obj.get("oneTimeToken"),
                "payment_request": PaymentRequest.from_dict(obj.get("paymentRequest"))
                if obj.get("paymentRequest") is not None
                else None,
            }
        )
        return _obj
