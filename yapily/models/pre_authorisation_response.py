# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.feature_enum import FeatureEnum

class PreAuthorisationResponse(BaseModel):
    """
    PreAuthorisationResponse
    """
    id: Optional[StrictStr] = Field(None, description="Unique identifier for the pre-authorisation request.")
    user_uuid: Optional[StrictStr] = Field(None, alias="userUuid", description="The `User` that the authorisation request was created for.")
    application_user_id: Optional[StrictStr] = Field(None, alias="applicationUserId", description="The user-friendly reference to the `User` that the authorisation request was created for.")
    reference_id: Optional[StrictStr] = Field(None, alias="referenceId")
    institution_id: Optional[StrictStr] = Field(None, alias="institutionId", description="The `Institution` the authorisation request was sent to.")
    status: Optional[AuthorisationStatus] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Date and time the consent was created.")
    transaction_from: Optional[datetime] = Field(None, alias="transactionFrom", description="When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved.")
    transaction_to: Optional[datetime] = Field(None, alias="transactionTo", description="When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved.")
    expires_at: Optional[datetime] = Field(None, alias="expiresAt", description="Date and time the authorisation expires. Re-authorisation is needed to retain access.")
    time_to_expire_in_millis: Optional[StrictInt] = Field(None, alias="timeToExpireInMillis")
    time_to_expire: Optional[StrictStr] = Field(None, alias="timeToExpire")
    feature_scope: Optional[conlist(FeatureEnum, unique_items=True)] = Field(None, alias="featureScope", description="The set of features the consent provides access to.")
    consent_token: Optional[StrictStr] = Field(None, alias="consentToken", description="Represents the authorisation to gain access to the requested features. Required to access account information or make a payment request.")
    state: Optional[StrictStr] = Field(None, description="Corellation ID used with the `Institution` during the authorisation process.")
    authorized_at: Optional[datetime] = Field(None, alias="authorizedAt", description="Date and time the request was authorised by the `Institution`.")
    institution_consent_id: Optional[StrictStr] = Field(None, alias="institutionConsentId", description="Unique identifier of the consent assigned by the `Institution`.")
    authorisation_url: Optional[StrictStr] = Field(None, alias="authorisationUrl")
    qr_code_url: Optional[StrictStr] = Field(None, alias="qrCodeUrl", description="The URL link for the QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded).")
    __properties = ["id", "userUuid", "applicationUserId", "referenceId", "institutionId", "status", "createdAt", "transactionFrom", "transactionTo", "expiresAt", "timeToExpireInMillis", "timeToExpire", "featureScope", "consentToken", "state", "authorizedAt", "institutionConsentId", "authorisationUrl", "qrCodeUrl"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PreAuthorisationResponse:
        """Create an instance of PreAuthorisationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreAuthorisationResponse:
        """Create an instance of PreAuthorisationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreAuthorisationResponse.parse_obj(obj)

        _obj = PreAuthorisationResponse.parse_obj({
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
            "qr_code_url": obj.get("qrCodeUrl")
        })
        return _obj


