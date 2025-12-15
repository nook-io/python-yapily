from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.hosted_consent_phase import HostedConsentPhase
from yapily.models.institution_identifiers_response import (
    InstitutionIdentifiersResponse,
)
from yapily.models.user_settings import UserSettings
from typing import Set
from typing_extensions import Self


class HostedGetConsentRequestResponse(BaseModel):
    consent_request_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique Id of the consent request.",
        alias="consentRequestId",
    )
    consent_id: Optional[StrictStr] = Field(
        default=None, description="Identification of the consent.", alias="consentId"
    )
    user_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique Id for the `User` assigned by Yapily.",
        alias="userId",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="Your reference to the `User`.",
        alias="applicationUserId",
    )
    application_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique Id of the `Application` the user is associated with.",
        alias="applicationId",
    )
    institution_identifiers: Optional[InstitutionIdentifiersResponse] = Field(
        default=None, alias="institutionIdentifiers"
    )
    user_settings: Optional[UserSettings] = Field(default=None, alias="userSettings")
    redirect_url: Optional[StrictStr] = Field(
        default=None,
        description="URL of consent server to redirect the user after completion of the consent flow.",
        alias="redirectUrl",
    )
    created_at: Optional[datetime] = Field(
        default=None,
        description="The date and time at which the payment was created.",
        alias="createdAt",
    )
    authorisation_expires_at: Optional[datetime] = Field(
        default=None,
        description="The date and time at which the auth Token will expire.",
        alias="authorisationExpiresAt",
    )
    status: Optional[StrictStr] = Field(
        default=None,
        description="Current status of the consent request. Allowed values are [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED, AWAITING_DECOUPLED_AUTHORIZATION]",
    )
    phases: Optional[List[HostedConsentPhase]] = Field(
        default=None, description="The phase reached by the consent and its timestamp."
    )
    consent_token: Optional[StrictStr] = Field(
        default=None,
        description="Represents the authorisation to gain access to the requested features. Required to access account information.",
        alias="consentToken",
    )
    __properties: ClassVar[List[str]] = [
        "consentRequestId",
        "consentId",
        "userId",
        "applicationUserId",
        "applicationId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "createdAt",
        "authorisationExpiresAt",
        "status",
        "phases",
        "consentToken",
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
        _items = []
        if self.phases:
            for _item_phases in self.phases:
                if _item_phases:
                    _items.append(_item_phases.to_dict())
            _dict["phases"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "consentRequestId": obj.get("consentRequestId"),
                "consentId": obj.get("consentId"),
                "userId": obj.get("userId"),
                "applicationUserId": obj.get("applicationUserId"),
                "applicationId": obj.get("applicationId"),
                "institutionIdentifiers": InstitutionIdentifiersResponse.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "userSettings": UserSettings.from_dict(obj["userSettings"])
                if obj.get("userSettings") is not None
                else None,
                "redirectUrl": obj.get("redirectUrl"),
                "createdAt": obj.get("createdAt"),
                "authorisationExpiresAt": obj.get("authorisationExpiresAt"),
                "status": obj.get("status"),
                "phases": [
                    HostedConsentPhase.from_dict(_item) for _item in obj["phases"]
                ]
                if obj.get("phases") is not None
                else None,
                "consentToken": obj.get("consentToken"),
            }
        )
        return _obj
