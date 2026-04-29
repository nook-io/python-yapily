import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr

from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.feature_enum import FeatureEnum
from yapily.validators import Unique


class Consent(BaseModel):
    """
    Consent detailing the requested authorisation from a user to a specific `Institution`.  # noqa: E501
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier of the consent.")] = None
    user_uuid: Annotated[StrictStr | None, Field(alias="userUuid")] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
        ),
    ] = None
    reference_id: Annotated[StrictStr | None, Field(alias="referenceId")] = None
    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId", description="__Mandatory__. The `Institution` the authorisation request is sent to."
        ),
    ] = None
    status: AuthorisationStatus | None = None
    created_at: Annotated[
        datetime | None, Field(alias="createdAt", description="Date and time of when the consent was created.")
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
            description="Date and time of when the authorisation will expire by. Reauthorisation will be needed to retain access.",
        ),
    ] = None
    time_to_expire_in_millis: Annotated[StrictInt | None, Field(alias="timeToExpireInMillis")] = None
    time_to_expire: Annotated[StrictStr | None, Field(alias="timeToExpire")] = None
    feature_scope: Annotated[
        Annotated[list[FeatureEnum], Unique] | None,
        Field(alias="featureScope", description="The set of features that the consent will provide access to."),
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
        Field(description="Correlation ID used with the `Institution` during the authorisation process."),
    ] = None
    authorized_at: Annotated[
        datetime | None,
        Field(alias="authorizedAt", description="Date and time of when the request was authorised by the Institution."),
    ] = None
    last_confirmed_at: Annotated[
        datetime | None,
        Field(
            alias="lastConfirmedAt",
            description="The time that the PSU last confirmed access to their account information, either through full authentication with the institution, or through reconfirmation with the TPP.",
        ),
    ] = None
    reconfirm_by: Annotated[
        datetime | None,
        Field(
            alias="reconfirmBy",
            description="The time by which the consent should be reconfirmed to ensure continued access to the account information.",
        ),
    ] = None
    institution_consent_id: Annotated[
        StrictStr | None,
        Field(alias="institutionConsentId", description="Identification of the consent at the Institution."),
    ] = None
    is_deleted_by_institution: Annotated[
        StrictBool | None,
        Field(
            alias="isDeletedByInstitution",
            description="Denotes whether the consent has been deleted on the institution side or not when a DELETE method is executed on a Yapily consent if that functionality is provided by the institution",
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
        "lastConfirmedAt",
        "reconfirmBy",
        "institutionConsentId",
        "isDeletedByInstitution",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Consent":
        """Create an instance of Consent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Consent":
        """Create an instance of Consent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Consent.model_validate(obj)

        return Consent.model_validate(
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
                "last_confirmed_at": obj.get("lastConfirmedAt"),
                "reconfirm_by": obj.get("reconfirmBy"),
                "institution_consent_id": obj.get("institutionConsentId"),
                "is_deleted_by_institution": obj.get("isDeletedByInstitution"),
            }
        )
