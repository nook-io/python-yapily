# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
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

class Consent(BaseModel):
    """
    Consent
    """
    id: Optional[StrictStr] = None
    user_uuid: Optional[StrictStr] = Field(None, alias="userUuid")
    application_user_id: Optional[StrictStr] = Field(None, alias="applicationUserId")
    reference_id: Optional[StrictStr] = Field(None, alias="referenceId")
    institution_id: Optional[StrictStr] = Field(None, alias="institutionId")
    status: Optional[AuthorisationStatus] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    transaction_from: Optional[datetime] = Field(None, alias="transactionFrom")
    transaction_to: Optional[datetime] = Field(None, alias="transactionTo")
    expires_at: Optional[datetime] = Field(None, alias="expiresAt")
    time_to_expire_in_millis: Optional[StrictInt] = Field(None, alias="timeToExpireInMillis")
    time_to_expire: Optional[StrictStr] = Field(None, alias="timeToExpire")
    feature_scope: Optional[conlist(FeatureEnum, unique_items=True)] = Field(None, alias="featureScope")
    consent_token: Optional[StrictStr] = Field(None, alias="consentToken")
    state: Optional[StrictStr] = None
    authorized_at: Optional[datetime] = Field(None, alias="authorizedAt")
    last_confirmed_at: Optional[datetime] = Field(None, alias="lastConfirmedAt", description="The time that the PSU last confirmed access to their account information, either through full authentication with the institution, or through reconfirmation with the TPP.")
    reconfirm_by: Optional[datetime] = Field(None, alias="reconfirmBy", description="The time by which the consent should be reconfirmed to ensure continued access to the account information.")
    institution_consent_id: Optional[StrictStr] = Field(None, alias="institutionConsentId")
    __properties = ["id", "userUuid", "applicationUserId", "referenceId", "institutionId", "status", "createdAt", "transactionFrom", "transactionTo", "expiresAt", "timeToExpireInMillis", "timeToExpire", "featureScope", "consentToken", "state", "authorizedAt", "lastConfirmedAt", "reconfirmBy", "institutionConsentId"]

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
    def from_json(cls, json_str: str) -> Consent:
        """Create an instance of Consent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Consent:
        """Create an instance of Consent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Consent.parse_obj(obj)

        _obj = Consent.parse_obj({
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
            "institution_consent_id": obj.get("institutionConsentId")
        })
        return _obj


