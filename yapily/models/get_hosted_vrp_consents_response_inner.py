import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.vrp_setup_request import VRPSetupRequest


class GetHostedVRPConsentsResponseInner(BaseModel):
    """
    GetHostedVRPConsentsResponseInner
    """

    id: Annotated[StrictStr, Field(description="Represents the Unique Id of the VRP consent request")]
    application_id: Annotated[
        StrictStr,
        Field(
            alias="applicationId",
            description="Represents the Unique Id of the `Application` the user is associated with.",
        ),
    ]
    institution_identifiers: Annotated[InstitutionIdentifiers | None, Field(alias="institutionIdentifiers")] = None
    vrp_setup: Annotated[VRPSetupRequest | None, Field(alias="vrpSetup")] = None
    updated_at: Annotated[
        datetime | None,
        Field(alias="updatedAt", description="Represents the date and time at which the Consent was updated."),
    ] = None
    consent_status: Annotated[
        StrictStr | None,
        Field(
            alias="consentStatus",
            description="Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED]",
        ),
    ] = None
    __properties = ["id", "applicationId", "institutionIdentifiers", "vrpSetup", "updatedAt", "consentStatus"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetHostedVRPConsentsResponseInner":
        """Create an instance of GetHostedVRPConsentsResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of institution_identifiers
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrp_setup
        if self.vrp_setup:
            _dict["vrpSetup"] = self.vrp_setup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetHostedVRPConsentsResponseInner":
        """Create an instance of GetHostedVRPConsentsResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetHostedVRPConsentsResponseInner.model_validate(obj)

        return GetHostedVRPConsentsResponseInner.model_validate(
            {
                "id": obj.get("id"),
                "application_id": obj.get("applicationId"),
                "institution_identifiers": InstitutionIdentifiers.from_dict(obj.get("institutionIdentifiers"))
                if obj.get("institutionIdentifiers") is not None
                else None,
                "vrp_setup": VRPSetupRequest.from_dict(obj.get("vrpSetup"))
                if obj.get("vrpSetup") is not None
                else None,
                "updated_at": obj.get("updatedAt"),
                "consent_status": obj.get("consentStatus"),
            }
        )
