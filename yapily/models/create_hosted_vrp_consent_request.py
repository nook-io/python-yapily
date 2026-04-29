import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings
from yapily.models.vrp_setup_request import VRPSetupRequest


class CreateHostedVRPConsentRequest(BaseModel):
    """
    CreateHostedVRPConsentRequest
    """

    user_id: Annotated[
        StrictStr | None,
        Field(
            alias="userId",
            description="__Conditional__. Yapily Identifier for the `User` returned by the create user step POST /users. Clients must either provide userId or applicationUserId.",
        ),
    ] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="__Conditional__. Client's own `User` reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value. Clients must either provide userId or applicationUserId.",
        ),
    ] = None
    institution_identifiers: Annotated[InstitutionIdentifiers, Field(alias="institutionIdentifiers")]
    user_settings: Annotated[UserSettings | None, Field(alias="userSettings")] = None
    redirect_url: Annotated[
        StrictStr,
        Field(
            alias="redirectUrl",
            description="URL of client's server to redirect the PSU after completion of the consent authorisation.",
        ),
    ]
    one_time_token: Annotated[
        StrictBool | None,
        Field(
            alias="oneTimeToken",
            description="Used to receive a oneTimeToken rather than a consentToken at the redirectUrl for additional security. This can only be used when the redirectUrl is set.",
        ),
    ] = None
    vrp_setup: Annotated[VRPSetupRequest, Field(alias="vrpSetup")]
    __properties = [
        "userId",
        "applicationUserId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "oneTimeToken",
        "vrpSetup",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CreateHostedVRPConsentRequest":
        """Create an instance of CreateHostedVRPConsentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
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
    def from_dict(cls, obj: dict) -> "CreateHostedVRPConsentRequest":
        """Create an instance of CreateHostedVRPConsentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateHostedVRPConsentRequest.model_validate(obj)

        return CreateHostedVRPConsentRequest.model_validate(
            {
                "user_id": obj.get("userId"),
                "application_user_id": obj.get("applicationUserId"),
                "institution_identifiers": InstitutionIdentifiers.from_dict(obj.get("institutionIdentifiers"))
                if obj.get("institutionIdentifiers") is not None
                else None,
                "user_settings": UserSettings.from_dict(obj.get("userSettings"))
                if obj.get("userSettings") is not None
                else None,
                "redirect_url": obj.get("redirectUrl"),
                "one_time_token": obj.get("oneTimeToken"),
                "vrp_setup": VRPSetupRequest.from_dict(obj.get("vrpSetup"))
                if obj.get("vrpSetup") is not None
                else None,
            }
        )
