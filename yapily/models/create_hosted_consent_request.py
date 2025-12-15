from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.hosted_account_request import HostedAccountRequest
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings
from typing import Set
from typing_extensions import Self


class CreateHostedConsentRequest(BaseModel):
    user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Yapily Identifier for the `User` returned by the create user step POST /users. You must provide either a `userId` or `applicationUserId`.",
        alias="userId",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Your own `User` reference. This field allows you to use your own unique references for individual users. Where the `User` reference doesn't have an associated Yapily `userId`, a new `userId` is created and linked to it. You must provide either a `userId` or `applicationUserId`.",
        alias="applicationUserId",
    )
    institution_identifiers: InstitutionIdentifiers = Field(
        alias="institutionIdentifiers"
    )
    user_settings: Optional[UserSettings] = Field(default=None, alias="userSettings")
    redirect_url: StrictStr = Field(
        description="URL of your server to redirect the user after completion of the consent flow.",
        alias="redirectUrl",
    )
    one_time_token: Optional[StrictBool] = Field(
        default=None,
        description="Used to receive a oneTimeToken rather than a consentToken at the redirectUrl for additional security.",
        alias="oneTimeToken",
    )
    account_request: Optional[HostedAccountRequest] = Field(
        default=None, alias="accountRequest"
    )
    __properties: ClassVar[List[str]] = [
        "userId",
        "applicationUserId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "oneTimeToken",
        "accountRequest",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        if self.user_settings:
            _dict["userSettings"] = self.user_settings.to_dict()
        if self.account_request:
            _dict["accountRequest"] = self.account_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "userId": obj.get("userId"),
                "applicationUserId": obj.get("applicationUserId"),
                "institutionIdentifiers": InstitutionIdentifiers.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "userSettings": UserSettings.from_dict(obj["userSettings"])
                if obj.get("userSettings") is not None
                else None,
                "redirectUrl": obj.get("redirectUrl"),
                "oneTimeToken": obj.get("oneTimeToken"),
                "accountRequest": HostedAccountRequest.from_dict(obj["accountRequest"])
                if obj.get("accountRequest") is not None
                else None,
            }
        )
        return _obj
