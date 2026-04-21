import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from yapily.models.hosted_account_request import HostedAccountRequest
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings


class CreateHostedConsentRequest(BaseModel):
    """
    CreateHostedConsentRequest
    """

    user_id: Annotated[
        StrictStr | None,
        Field(
            alias="userId",
            description="__Conditional__. Yapily Identifier for the `User` returned by the create user step POST /users. You must provide either a `userId` or `applicationUserId`.",
        ),
    ] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="__Conditional__. Your own `User` reference. This field allows you to use your own unique references for individual users. Where the `User` reference doesn't have an associated Yapily `userId`, a new `userId` is created and linked to it. You must provide either a `userId` or `applicationUserId`.",
        ),
    ] = None
    institution_identifiers: Annotated[InstitutionIdentifiers, Field(alias="institutionIdentifiers")]
    user_settings: Annotated[UserSettings | None, Field(alias="userSettings")] = None
    redirect_url: Annotated[
        StrictStr,
        Field(
            alias="redirectUrl",
            description="URL of your server to redirect the user after completion of the consent flow.",
        ),
    ]
    one_time_token: Annotated[
        StrictBool | None,
        Field(
            alias="oneTimeToken",
            description="Used to receive a oneTimeToken rather than a consentToken at the redirectUrl for additional security.",
        ),
    ] = None
    account_request: Annotated[HostedAccountRequest | None, Field(alias="accountRequest")] = None
    __properties = [
        "userId",
        "applicationUserId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "oneTimeToken",
        "accountRequest",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CreateHostedConsentRequest":
        """Create an instance of CreateHostedConsentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_request
        if self.account_request:
            _dict["accountRequest"] = self.account_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "CreateHostedConsentRequest":
        """Create an instance of CreateHostedConsentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateHostedConsentRequest.parse_obj(obj)

        return CreateHostedConsentRequest.parse_obj(
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
                "account_request": HostedAccountRequest.from_dict(obj.get("accountRequest"))
                if obj.get("accountRequest") is not None
                else None,
            }
        )
