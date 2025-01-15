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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from yapily.models.bulk_payment_request import BulkPaymentRequest
from yapily.models.redirect_request import RedirectRequest
from yapily.models.sca_method import ScaMethod
from yapily.models.user_credentials import UserCredentials


class BulkPaymentEmbeddedAuthorisationRequest(BaseModel):
    """
    The request body containing a `BulkPaymentEmbeddedAuthorisationRequest` json payload  # noqa: E501
    """

    user_uuid: Optional[StrictStr] = Field(
        default=None,
        alias="userUuid",
        description="__Conditional__. The reference to the `User` that will authorise the authorisation request using the Yapily generated UUID. Either the `userUuid` or `applicationUserId` must be provided.",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        alias="applicationUserId",
        description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
    )
    institution_id: StrictStr = Field(
        default=...,
        alias="institutionId",
        description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.",
    )
    callback: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for more information.",
    )
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(
        default=None,
        alias="oneTimeToken",
        description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.",
    )
    payment_request: Optional[BulkPaymentRequest] = Field(
        default=None, alias="paymentRequest"
    )
    user_credentials: Optional[UserCredentials] = Field(
        default=None, alias="userCredentials"
    )
    selected_sca_method: Optional[ScaMethod] = Field(
        default=None, alias="selectedScaMethod"
    )
    sca_code: Optional[StrictStr] = Field(
        default=None,
        alias="scaCode",
        description="__Conditional__. Used to update the authorisation with the sca code received by the user from the `Institution` using the embedded payment authorisation flow.<br><br>This is the penultimate step required in the embedded payment authorisation flow to authorise the `Consent`. After sending the sca code, to obtain an authorised consent, the last step is to poll [Get Consent](https://docs.yapily.com/api/reference/#operation/getConsentById) until the `Institution` authorises the request and the `Consent` `status` transitions to `AUTHORIZED`.",
    )
    __properties = [
        "userUuid",
        "applicationUserId",
        "institutionId",
        "callback",
        "redirect",
        "oneTimeToken",
        "paymentRequest",
        "userCredentials",
        "selectedScaMethod",
        "scaCode",
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
    def from_json(cls, json_str: str) -> BulkPaymentEmbeddedAuthorisationRequest:
        """Create an instance of BulkPaymentEmbeddedAuthorisationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_credentials
        if self.user_credentials:
            _dict["userCredentials"] = self.user_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selected_sca_method
        if self.selected_sca_method:
            _dict["selectedScaMethod"] = self.selected_sca_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BulkPaymentEmbeddedAuthorisationRequest:
        """Create an instance of BulkPaymentEmbeddedAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BulkPaymentEmbeddedAuthorisationRequest.parse_obj(obj)

        _obj = BulkPaymentEmbeddedAuthorisationRequest.parse_obj(
            {
                "user_uuid": obj.get("userUuid"),
                "application_user_id": obj.get("applicationUserId"),
                "institution_id": obj.get("institutionId"),
                "callback": obj.get("callback"),
                "redirect": RedirectRequest.from_dict(obj.get("redirect"))
                if obj.get("redirect") is not None
                else None,
                "one_time_token": obj.get("oneTimeToken"),
                "payment_request": BulkPaymentRequest.from_dict(
                    obj.get("paymentRequest")
                )
                if obj.get("paymentRequest") is not None
                else None,
                "user_credentials": UserCredentials.from_dict(
                    obj.get("userCredentials")
                )
                if obj.get("userCredentials") is not None
                else None,
                "selected_sca_method": ScaMethod.from_dict(obj.get("selectedScaMethod"))
                if obj.get("selectedScaMethod") is not None
                else None,
                "sca_code": obj.get("scaCode"),
            }
        )
        return _obj
