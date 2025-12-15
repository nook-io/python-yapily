from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.vrp_setup_request import VRPSetupRequest
from typing import Set
from typing_extensions import Self


class GetHostedVRPConsentsResponseInner(BaseModel):
    id: StrictStr = Field(
        description="Represents the Unique Id of the VRP consent request"
    )
    application_id: StrictStr = Field(
        description="Represents the Unique Id of the `Application` the user is associated with.",
        alias="applicationId",
    )
    institution_identifiers: Optional[InstitutionIdentifiers] = Field(
        default=None, alias="institutionIdentifiers"
    )
    vrp_setup: Optional[VRPSetupRequest] = Field(default=None, alias="vrpSetup")
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Represents the date and time at which the Consent was updated.",
        alias="updatedAt",
    )
    consent_status: Optional[StrictStr] = Field(
        default=None,
        description="Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED]",
        alias="consentStatus",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "applicationId",
        "institutionIdentifiers",
        "vrpSetup",
        "updatedAt",
        "consentStatus",
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
        if self.vrp_setup:
            _dict["vrpSetup"] = self.vrp_setup.to_dict()
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
                "applicationId": obj.get("applicationId"),
                "institutionIdentifiers": InstitutionIdentifiers.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "vrpSetup": VRPSetupRequest.from_dict(obj["vrpSetup"])
                if obj.get("vrpSetup") is not None
                else None,
                "updatedAt": obj.get("updatedAt"),
                "consentStatus": obj.get("consentStatus"),
            }
        )
        return _obj
