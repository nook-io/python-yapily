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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings
from yapily.models.vrp_setup_request import VRPSetupRequest
from typing import Set
from typing_extensions import Self


class HostedVRPConsentRequestResponse(BaseModel):
    """
    HostedVRPConsentRequestResponse
    """  # noqa: E501

    id: StrictStr = Field(
        description="Represents the Unique Id of the VRP consent request"
    )
    user_id: Optional[StrictStr] = Field(
        default=None,
        description="Represents the Unique Id for the `User` assigned by Yapily.",
        alias="userId",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="Represents the user-friendly reference to the `User`.",
        alias="applicationUserId",
    )
    application_id: StrictStr = Field(
        description="Represents the Unique Id of the `Application` the user is associated with.",
        alias="applicationId",
    )
    institution_identifiers: Optional[InstitutionIdentifiers] = Field(
        default=None, alias="institutionIdentifiers"
    )
    user_settings: Optional[UserSettings] = Field(default=None, alias="userSettings")
    redirect_url: Optional[StrictStr] = Field(
        default=None,
        description="URL of client's server to redirect the PSU after completion of the consent authorisation.",
        alias="redirectUrl",
    )
    vrp_setup: Optional[VRPSetupRequest] = Field(default=None, alias="vrpSetup")
    hosted_url: StrictStr = Field(
        description="Represents the URL of Hosted UI page for the applicationId which initiates the user journey for the Consent. <br> URL would be appended with authToken, applicationId and userSettings.",
        alias="hostedUrl",
    )
    auth_token: StrictStr = Field(
        description="Represents the JWT Token signed by the certificate-vault using Yapily's keys.",
        alias="authToken",
    )
    created_at: datetime = Field(
        description="Represents the date and time at which the Consent was created.",
        alias="createdAt",
    )
    authorisation_expires_at: Optional[datetime] = Field(
        default=None,
        description="Represents the date and time at which the auth Token will expire.",
        alias="authorisationExpiresAt",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "userId",
        "applicationUserId",
        "applicationId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "vrpSetup",
        "hostedUrl",
        "authToken",
        "createdAt",
        "authorisationExpiresAt",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HostedVRPConsentRequestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of institution_identifiers
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_settings
        if self.user_settings:
            _dict["userSettings"] = self.user_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrp_setup
        if self.vrp_setup:
            _dict["vrpSetup"] = self.vrp_setup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostedVRPConsentRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "userId": obj.get("userId"),
                "applicationUserId": obj.get("applicationUserId"),
                "applicationId": obj.get("applicationId"),
                "institutionIdentifiers": InstitutionIdentifiers.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "userSettings": UserSettings.from_dict(obj["userSettings"])
                if obj.get("userSettings") is not None
                else None,
                "redirectUrl": obj.get("redirectUrl"),
                "vrpSetup": VRPSetupRequest.from_dict(obj["vrpSetup"])
                if obj.get("vrpSetup") is not None
                else None,
                "hostedUrl": obj.get("hostedUrl"),
                "authToken": obj.get("authToken"),
                "createdAt": obj.get("createdAt"),
                "authorisationExpiresAt": obj.get("authorisationExpiresAt"),
            }
        )
        return _obj
