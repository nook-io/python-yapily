import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.exchange_rate_information_response import ExchangeRateInformationResponse
from yapily.models.feature_enum import FeatureEnum
from yapily.models.payment_charge_details import PaymentChargeDetails
from yapily.validators import Unique


class PaymentAuthorisationRequestResponse(BaseModel):
    """
    PaymentAuthorisationRequestResponse
    """

    id: Annotated[
        StrictStr | None,
        Field(
            description="Unique identifier for the payment authorisation request. <br><br>The `consentID` used to [retrieve a consent](/api/reference/#operation/getConsentById)."
        ),
    ] = None
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
            description="Represents the authorisation to gain access to the requested features. Required to make a payment request.",
        ),
    ] = None
    state: Annotated[
        StrictStr | None,
        Field(description="Correlation ID used with the `Institution` during the authorisation process."),
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
    charges: Annotated[list[PaymentChargeDetails], Field()] | None = None
    exchange_rate_information: Annotated[
        ExchangeRateInformationResponse | None, Field(alias="exchangeRateInformation")
    ] = None
    authorisation_url: Annotated[StrictStr | None, Field(alias="authorisationUrl")] = None
    qr_code_url: Annotated[
        StrictStr | None,
        Field(
            alias="qrCodeUrl",
            description="The URL for a QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded).",
        ),
    ] = None
    explanation: Annotated[
        StrictStr | None,
        Field(
            description="Message from the `Institution` received by Yapily, detailing the next action the user is required to take. This is used only for Decoupled flows."
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
        "charges",
        "exchangeRateInformation",
        "authorisationUrl",
        "qrCodeUrl",
        "explanation",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentAuthorisationRequestResponse":
        """Create an instance of PaymentAuthorisationRequestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item in self.charges:
                if _item:
                    _items.append(_item.to_dict())
            _dict["charges"] = _items
        # override the default output from pydantic by calling `to_dict()` of exchange_rate_information
        if self.exchange_rate_information:
            _dict["exchangeRateInformation"] = self.exchange_rate_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "PaymentAuthorisationRequestResponse":
        """Create an instance of PaymentAuthorisationRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentAuthorisationRequestResponse.model_validate(obj)

        return PaymentAuthorisationRequestResponse.model_validate(
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
                "charges": [PaymentChargeDetails.from_dict(_item) for _item in obj.get("charges")]
                if obj.get("charges") is not None
                else None,
                "exchange_rate_information": ExchangeRateInformationResponse.from_dict(
                    obj.get("exchangeRateInformation")
                )
                if obj.get("exchangeRateInformation") is not None
                else None,
                "authorisation_url": obj.get("authorisationUrl"),
                "qr_code_url": obj.get("qrCodeUrl"),
                "explanation": obj.get("explanation"),
            }
        )
