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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.hosted_payment_request_details_link import (
    HostedPaymentRequestDetailsLink,
)
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings


class CreateHostedPaymentRequestLink(BaseModel):
    """
    CreateHostedPaymentRequestLink
    """

    user_id: Optional[StrictStr] = Field(
        default=None,
        alias="userId",
        description="__Conditional__. Yapily Identifier for the `User` returned by the create user step POST /users. You must either provide `userId` or `applicationUserId`.",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        alias="applicationUserId",
        description="__Conditional__. Your own `User` reference. If you want to work with their own unique references for individual PSUs then you can use the `applicationUserId` property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied `applicationUserId`, then a new Yapily userId is created automatically and linked to the `applicationUserId` value. You must either provide userId or `applicationUserId`.",
    )
    institution_identifiers: InstitutionIdentifiers = Field(
        default=..., alias="institutionIdentifiers"
    )
    user_settings: Optional[UserSettings] = Field(default=None, alias="userSettings")
    redirect_url: StrictStr = Field(
        default=...,
        alias="redirectUrl",
        description="URL of your server to redirect the user after completion of the payment flow.",
    )
    authorisation_expires_at: Optional[datetime] = Field(
        default=None,
        alias="authorisationExpiresAt",
        description="The date and time that the authorisation expires. Must be between 10 minutes and 30 days in the future. If not specified, the authorisation URL will expire 10 minutes after creation.",
    )
    payment_request_details: HostedPaymentRequestDetailsLink = Field(
        default=..., alias="paymentRequestDetails"
    )
    __properties = [
        "userId",
        "applicationUserId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "authorisationExpiresAt",
        "paymentRequestDetails",
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
    def from_json(cls, json_str: str) -> CreateHostedPaymentRequestLink:
        """Create an instance of CreateHostedPaymentRequestLink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of institution_identifiers
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_settings
        if self.user_settings:
            _dict["userSettings"] = self.user_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_request_details
        if self.payment_request_details:
            _dict["paymentRequestDetails"] = self.payment_request_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateHostedPaymentRequestLink:
        """Create an instance of CreateHostedPaymentRequestLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateHostedPaymentRequestLink.parse_obj(obj)

        _obj = CreateHostedPaymentRequestLink.parse_obj(
            {
                "user_id": obj.get("userId"),
                "application_user_id": obj.get("applicationUserId"),
                "institution_identifiers": InstitutionIdentifiers.from_dict(
                    obj.get("institutionIdentifiers")
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "user_settings": UserSettings.from_dict(obj.get("userSettings"))
                if obj.get("userSettings") is not None
                else None,
                "redirect_url": obj.get("redirectUrl"),
                "authorisation_expires_at": obj.get("authorisationExpiresAt"),
                "payment_request_details": HostedPaymentRequestDetailsLink.from_dict(
                    obj.get("paymentRequestDetails")
                )
                if obj.get("paymentRequestDetails") is not None
                else None,
            }
        )
        return _obj
