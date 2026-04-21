import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.hosted_account_request_details_response import HostedAccountRequestDetailsResponse
from yapily.models.institution_identifiers_response import InstitutionIdentifiersResponse
from yapily.models.user_settings import UserSettings


class HostedConsentRequestResponse(BaseModel):
    """
    HostedConsentRequestResponse
    """

    consent_request_id: Annotated[
        StrictStr | None, Field(alias="consentRequestId", description="Unique Id of the consent request.")
    ] = None
    user_id: Annotated[
        StrictStr | None, Field(alias="userId", description="Unique Id for the `User` assigned by Yapily.")
    ] = None
    application_user_id: Annotated[
        StrictStr | None, Field(alias="applicationUserId", description="Your reference to the `User`.")
    ] = None
    application_id: Annotated[
        StrictStr | None,
        Field(alias="applicationId", description="Unique Id of the `Application` the user is associated with."),
    ] = None
    institution_identifiers: Annotated[InstitutionIdentifiersResponse | None, Field(alias="institutionIdentifiers")] = (
        None
    )
    user_settings: Annotated[UserSettings | None, Field(alias="userSettings")] = None
    redirect_url: Annotated[
        StrictStr | None,
        Field(
            alias="redirectUrl",
            description="URL of consent server to redirect the user after completion of the consent flow.",
        ),
    ] = None
    account_request_details: Annotated[
        HostedAccountRequestDetailsResponse | None, Field(alias="accountRequestDetails")
    ] = None
    hosted_url: Annotated[
        StrictStr | None,
        Field(
            alias="hostedUrl",
            description="The URL of Hosted UI page for the applicationId which initiates the user journey for the consent. <br> URL would be appended with authToken, applicationId and userSettings.",
        ),
    ] = None
    created_at: Annotated[
        datetime | None, Field(alias="createdAt", description="The date and time at which the consent was created.")
    ] = None
    authorisation_expires_at: Annotated[
        datetime | None,
        Field(alias="authorisationExpiresAt", description="The date and time at which the auth Token will expire."),
    ] = None
    __properties = [
        "consentRequestId",
        "userId",
        "applicationUserId",
        "applicationId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "accountRequestDetails",
        "hostedUrl",
        "createdAt",
        "authorisationExpiresAt",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedConsentRequestResponse":
        """Create an instance of HostedConsentRequestResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_request_details
        if self.account_request_details:
            _dict["accountRequestDetails"] = self.account_request_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedConsentRequestResponse":
        """Create an instance of HostedConsentRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedConsentRequestResponse.parse_obj(obj)

        return HostedConsentRequestResponse.parse_obj(
            {
                "consent_request_id": obj.get("consentRequestId"),
                "user_id": obj.get("userId"),
                "application_user_id": obj.get("applicationUserId"),
                "application_id": obj.get("applicationId"),
                "institution_identifiers": InstitutionIdentifiersResponse.from_dict(obj.get("institutionIdentifiers"))
                if obj.get("institutionIdentifiers") is not None
                else None,
                "user_settings": UserSettings.from_dict(obj.get("userSettings"))
                if obj.get("userSettings") is not None
                else None,
                "redirect_url": obj.get("redirectUrl"),
                "account_request_details": HostedAccountRequestDetailsResponse.from_dict(
                    obj.get("accountRequestDetails")
                )
                if obj.get("accountRequestDetails") is not None
                else None,
                "hosted_url": obj.get("hostedUrl"),
                "created_at": obj.get("createdAt"),
                "authorisation_expires_at": obj.get("authorisationExpiresAt"),
            }
        )
