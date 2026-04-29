import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.feature_enum import FeatureEnum
from yapily.models.initiation_details import InitiationDetails
from yapily.models.payer import Payer
from yapily.models.sweeping_control_parameters import SweepingControlParameters
from yapily.validators import Unique


class SweepingAuthorisationResponse(BaseModel):
    """
    SweepingAuthorisationResponse
    """

    id: StrictStr | None = None
    user_id: Annotated[
        StrictStr | None,
        Field(
            alias="userId",
            description="This is the Yapily user identifier for the user returned by the create user step POST ../users",
        ),
    ] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="A client's own user reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use either their own applicationUserId or the Yapily userId to reference the same user in future calls.",
        ),
    ] = None
    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId",
            description="The reference to the Institution which identifies which institution the authorisation request is sent to.",
        ),
    ] = None
    status: AuthorisationStatus | None = None
    created_at: Annotated[datetime | None, Field(alias="createdAt")] = None
    feature_scope: Annotated[
        Annotated[list[FeatureEnum], Unique] | None,
        Field(
            alias="featureScope",
            description="__Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).",
        ),
    ] = None
    consent_token: Annotated[
        StrictStr | None,
        Field(
            alias="consentToken",
            description="The `consent-token` containing the user's authorisation to make the payment request.",
        ),
    ] = None
    state: StrictStr | None = None
    authorized_at: Annotated[datetime | None, Field(alias="authorizedAt")] = None
    institution_consent_id: Annotated[
        StrictStr | None,
        Field(alias="institutionConsentId", description="Identification of the consent at the Institution."),
    ] = None
    authorisation_url: Annotated[StrictStr | None, Field(alias="authorisationUrl")] = None
    qr_code_url: Annotated[StrictStr | None, Field(alias="qrCodeUrl")] = None
    control_parameters: Annotated[SweepingControlParameters | None, Field(alias="controlParameters")] = None
    payer: Payer | None = None
    initiation_details: Annotated[InitiationDetails | None, Field(alias="initiationDetails")] = None
    __properties = [
        "id",
        "userId",
        "applicationUserId",
        "institutionId",
        "status",
        "createdAt",
        "featureScope",
        "consentToken",
        "state",
        "authorizedAt",
        "institutionConsentId",
        "authorisationUrl",
        "qrCodeUrl",
        "controlParameters",
        "payer",
        "initiationDetails",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SweepingAuthorisationResponse":
        """Create an instance of SweepingAuthorisationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of control_parameters
        if self.control_parameters:
            _dict["controlParameters"] = self.control_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initiation_details
        if self.initiation_details:
            _dict["initiationDetails"] = self.initiation_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "SweepingAuthorisationResponse":
        """Create an instance of SweepingAuthorisationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SweepingAuthorisationResponse.model_validate(obj)

        return SweepingAuthorisationResponse.model_validate(
            {
                "id": obj.get("id"),
                "user_id": obj.get("userId"),
                "application_user_id": obj.get("applicationUserId"),
                "institution_id": obj.get("institutionId"),
                "status": obj.get("status"),
                "created_at": obj.get("createdAt"),
                "feature_scope": obj.get("featureScope"),
                "consent_token": obj.get("consentToken"),
                "state": obj.get("state"),
                "authorized_at": obj.get("authorizedAt"),
                "institution_consent_id": obj.get("institutionConsentId"),
                "authorisation_url": obj.get("authorisationUrl"),
                "qr_code_url": obj.get("qrCodeUrl"),
                "control_parameters": SweepingControlParameters.from_dict(obj.get("controlParameters"))
                if obj.get("controlParameters") is not None
                else None,
                "payer": Payer.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
                "initiation_details": InitiationDetails.from_dict(obj.get("initiationDetails"))
                if obj.get("initiationDetails") is not None
                else None,
            }
        )
