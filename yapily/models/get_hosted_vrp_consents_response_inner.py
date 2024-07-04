# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.vrp_setup_request import VRPSetupRequest

class GetHostedVRPConsentsResponseInner(BaseModel):
    """
    GetHostedVRPConsentsResponseInner
    """
    id: StrictStr = Field(..., description="Represents the Unique Id of the VRP consent request")
    application_id: StrictStr = Field(..., alias="applicationId", description="Represents the Unique Id of the `Application` the user is associated with.")
    institution_identifiers: Optional[InstitutionIdentifiers] = Field(None, alias="institutionIdentifiers")
    vrp_setup: Optional[VRPSetupRequest] = Field(None, alias="vrpSetup")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="Represents the date and time at which the Consent was updated.")
    consent_status: Optional[StrictStr] = Field(None, alias="consentStatus", description="Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED]")
    __properties = ["id", "applicationId", "institutionIdentifiers", "vrpSetup", "updatedAt", "consentStatus"]

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
    def from_json(cls, json_str: str) -> GetHostedVRPConsentsResponseInner:
        """Create an instance of GetHostedVRPConsentsResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of institution_identifiers
        if self.institution_identifiers:
            _dict['institutionIdentifiers'] = self.institution_identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrp_setup
        if self.vrp_setup:
            _dict['vrpSetup'] = self.vrp_setup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetHostedVRPConsentsResponseInner:
        """Create an instance of GetHostedVRPConsentsResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetHostedVRPConsentsResponseInner.parse_obj(obj)

        _obj = GetHostedVRPConsentsResponseInner.parse_obj({
            "id": obj.get("id"),
            "application_id": obj.get("applicationId"),
            "institution_identifiers": InstitutionIdentifiers.from_dict(obj.get("institutionIdentifiers")) if obj.get("institutionIdentifiers") is not None else None,
            "vrp_setup": VRPSetupRequest.from_dict(obj.get("vrpSetup")) if obj.get("vrpSetup") is not None else None,
            "updated_at": obj.get("updatedAt"),
            "consent_status": obj.get("consentStatus")
        })
        return _obj

