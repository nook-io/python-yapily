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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from yapily.models.initiation_details import InitiationDetails
from yapily.models.payment_context_type import PaymentContextType
from yapily.models.redirect_request import RedirectRequest
from yapily.models.sweeping_control_parameters import SweepingControlParameters

class SweepingAuthorisationRequest(BaseModel):
    """
    SweepingAuthorisationRequest
    """
    user_id: Optional[StrictStr] = Field(None, alias="userId", description="This is the Yapily user identifier for the user returned by the create user step POST ../users")
    application_user_id: Optional[StrictStr] = Field(None, alias="applicationUserId", description="A client's own user reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use either their own applicationUserId or the Yapily userId to reference the same user in future calls.")
    forward_parameters: Optional[conlist(StrictStr)] = Field(None, alias="forwardParameters", description="Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect.")
    context_type: Optional[PaymentContextType] = Field(None, alias="contextType")
    institution_id: StrictStr = Field(..., alias="institutionId", description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.")
    callback: Optional[StrictStr] = Field(None, description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-optional) for more information.")
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(None, alias="oneTimeToken", description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-with-an-ott-optional) for more information.")
    control_parameters: SweepingControlParameters = Field(..., alias="controlParameters")
    initiation_details: InitiationDetails = Field(..., alias="initiationDetails")
    __properties = ["userId", "applicationUserId", "forwardParameters", "contextType", "institutionId", "callback", "redirect", "oneTimeToken", "controlParameters", "initiationDetails"]

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
    def from_json(cls, json_str: str) -> SweepingAuthorisationRequest:
        """Create an instance of SweepingAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of redirect
        if self.redirect:
            _dict['redirect'] = self.redirect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of control_parameters
        if self.control_parameters:
            _dict['controlParameters'] = self.control_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of initiation_details
        if self.initiation_details:
            _dict['initiationDetails'] = self.initiation_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SweepingAuthorisationRequest:
        """Create an instance of SweepingAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SweepingAuthorisationRequest.parse_obj(obj)

        _obj = SweepingAuthorisationRequest.parse_obj({
            "user_id": obj.get("userId"),
            "application_user_id": obj.get("applicationUserId"),
            "forward_parameters": obj.get("forwardParameters"),
            "context_type": obj.get("contextType"),
            "institution_id": obj.get("institutionId"),
            "callback": obj.get("callback"),
            "redirect": RedirectRequest.from_dict(obj.get("redirect")) if obj.get("redirect") is not None else None,
            "one_time_token": obj.get("oneTimeToken"),
            "control_parameters": SweepingControlParameters.from_dict(obj.get("controlParameters")) if obj.get("controlParameters") is not None else None,
            "initiation_details": InitiationDetails.from_dict(obj.get("initiationDetails")) if obj.get("initiationDetails") is not None else None
        })
        return _obj


