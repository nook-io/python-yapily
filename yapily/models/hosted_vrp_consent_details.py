from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.hosted_vrp_phase import HostedVRPPhase
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings
from yapily.models.vrp_setup import VRPSetup
from typing import Set
from typing_extensions import Self


class HostedVRPConsentDetails(BaseModel):
    id: StrictStr = Field(description="The unique ID of the consent request.")
    user_id: Optional[StrictStr] = Field(
        default=None,
        description="Represents the Unique Identifier for the `User` assigned by Yapily.",
        alias="userId",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="Represents the User-friendly reference to the `User`.",
        alias="applicationUserId",
    )
    application_id: StrictStr = Field(
        description="Represens the Unique Identifier of the `Application` the user is associated with.",
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
    vrp_setup: VRPSetup = Field(alias="vrpSetup")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    authorisation_expires_at: Optional[datetime] = Field(
        default=None,
        description="Represents the date and time at which the auth Token will expire.",
        alias="authorisationExpiresAt",
    )
    consent_token: Optional[StrictStr] = Field(
        default=None,
        description="Represents the authorisation to make VRP payments",
        alias="consentToken",
    )
    consent_status: StrictStr = Field(
        description="Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED]",
        alias="consentStatus",
    )
    phases: Optional[List[HostedVRPPhase]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "userId",
        "applicationUserId",
        "applicationId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "vrpSetup",
        "createdAt",
        "authorisationExpiresAt",
        "consentToken",
        "consentStatus",
        "phases",
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
        if self.vrp_setup:
            _dict["vrpSetup"] = self.vrp_setup.to_dict()
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
                "vrpSetup": VRPSetup.from_dict(obj["vrpSetup"])
                if obj.get("vrpSetup") is not None
                else None,
                "createdAt": obj.get("createdAt"),
                "authorisationExpiresAt": obj.get("authorisationExpiresAt"),
                "consentToken": obj.get("consentToken"),
                "consentStatus": obj.get("consentStatus"),
                "phases": [HostedVRPPhase.from_dict(_item) for _item in obj["phases"]]
                if obj.get("phases") is not None
                else None,
            }
        )
        return _obj
