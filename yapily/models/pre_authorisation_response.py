import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.feature_enum import FeatureEnum
from yapily.validators import Unique


class PreAuthorisationResponse(BaseModel):
    """
    PreAuthorisationResponse
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier for the pre-authorisation request.")] = None
    user_uuid: Annotated[
        StrictStr | None,
        Field(alias="userUuid", description="The `User` that the authorisation request was created for."),
    ] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="The user-friendly reference to the `User` that the authorisation request was created for.",
        ),
    ] = None
    reference_id: Annotated[StrictStr | None, Field(alias="referenceId")] = None
    institution_id: Annotated[
        StrictStr | None,
        Field(alias="institutionId", description="The `Institution` the authorisation request was sent to."),
    ] = None
    status: AuthorisationStatus | None = None
    created_at: Annotated[
        datetime | None, Field(alias="createdAt", description="Date and time the consent was created.")
    ] = None
    transaction_from: Annotated[
        datetime | None,
        Field(
            alias="transactionFrom",
            description="When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved.",
        ),
    ] = None
    transaction_to: Annotated[
        datetime | None,
        Field(
            alias="transactionTo",
            description="When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved.",
        ),
    ] = None
    expires_at: Annotated[
        datetime | None,
        Field(
            alias="expiresAt",
            description="Date and time the authorisation expires. Re-authorisation is needed to retain access.",
        ),
    ] = None
    time_to_expire_in_millis: Annotated[StrictInt | None, Field(alias="timeToExpireInMillis")] = None
    time_to_expire: Annotated[StrictStr | None, Field(alias="timeToExpire")] = None
    feature_scope: Annotated[
        Annotated[list[FeatureEnum], Unique] | None,
        Field(alias="featureScope", description="The set of features the consent provides access to."),
    ] = None
    consent_token: Annotated[
        StrictStr | None,
        Field(
            alias="consentToken",
            description="Represents the authorisation to gain access to the requested features. Required to access account information or make a payment request.",
        ),
    ] = None
    state: Annotated[
        StrictStr | None,
        Field(description="Corellation ID used with the `Institution` during the authorisation process."),
    ] = None
    authorized_at: Annotated[
        datetime | None,
        Field(alias="authorizedAt", description="Date and time the request was authorised by the `Institution`."),
    ] = None
    institution_consent_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionConsentId", description="Unique identifier of the consent assigned by the `Institution`."
        ),
    ] = None
    authorisation_url: Annotated[StrictStr | None, Field(alias="authorisationUrl")] = None
    qr_code_url: Annotated[
        StrictStr | None,
        Field(
            alias="qrCodeUrl",
            description="The URL link for the QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded).",
        ),
    ] = None
    __properties = [
        "id",
        "userUuid",
        "applicationUserId",
        "referenceId",
        "institutionId",
        "status",
        "createdAt",
        "transactionFrom",
        "transactionTo",
        "expiresAt",
        "timeToExpireInMillis",
        "timeToExpire",
        "featureScope",
        "consentToken",
        "state",
        "authorizedAt",
        "institutionConsentId",
        "authorisationUrl",
        "qrCodeUrl",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PreAuthorisationResponse":
        """Create an instance of PreAuthorisationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "PreAuthorisationResponse":
        """Create an instance of PreAuthorisationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreAuthorisationResponse.model_validate(obj)

        return PreAuthorisationResponse.model_validate(
            {
                "id": obj.get("id"),
                "user_uuid": obj.get("userUuid"),
                "application_user_id": obj.get("applicationUserId"),
                "reference_id": obj.get("referenceId"),
                "institution_id": obj.get("institutionId"),
                "status": obj.get("status"),
                "created_at": obj.get("createdAt"),
                "transaction_from": obj.get("transactionFrom"),
                "transaction_to": obj.get("transactionTo"),
                "expires_at": obj.get("expiresAt"),
                "time_to_expire_in_millis": obj.get("timeToExpireInMillis"),
                "time_to_expire": obj.get("timeToExpire"),
                "feature_scope": obj.get("featureScope"),
                "consent_token": obj.get("consentToken"),
                "state": obj.get("state"),
                "authorized_at": obj.get("authorizedAt"),
                "institution_consent_id": obj.get("institutionConsentId"),
                "authorisation_url": obj.get("authorisationUrl"),
                "qr_code_url": obj.get("qrCodeUrl"),
            }
        )
