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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from yapily.models.initiation_details import InitiationDetails
from yapily.models.payment_context_type import PaymentContextType
from yapily.models.redirect_request import RedirectRequest
from yapily.models.sweeping_control_parameters import SweepingControlParameters
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SweepingAuthorisationRequest(BaseModel):
    """
    SweepingAuthorisationRequest
    """ # noqa: E501
    user_id: Optional[StrictStr] = Field(default=None, description="This is the Yapily user identifier for the user returned by the create user step POST ../users", alias="userId")
    application_user_id: Optional[StrictStr] = Field(default=None, description="A client's own user reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use either their own applicationUserId or the Yapily userId to reference the same user in future calls.", alias="applicationUserId")
    forward_parameters: Optional[List[StrictStr]] = Field(default=None, description="Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect.", alias="forwardParameters")
    context_type: Optional[PaymentContextType] = Field(default=None, alias="contextType")
    institution_id: StrictStr = Field(description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.", alias="institutionId")
    callback: Optional[StrictStr] = Field(default=None, description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-optional) for more information.")
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(default=None, description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-with-an-ott-optional) for more information.", alias="oneTimeToken")
    control_parameters: SweepingControlParameters = Field(alias="controlParameters")
    initiation_details: InitiationDetails = Field(alias="initiationDetails")
    __properties: ClassVar[List[str]] = ["userId", "applicationUserId", "forwardParameters", "contextType", "institutionId", "callback", "redirect", "oneTimeToken", "controlParameters", "initiationDetails"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SweepingAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SweepingAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userId": obj.get("userId"),
            "applicationUserId": obj.get("applicationUserId"),
            "forwardParameters": obj.get("forwardParameters"),
            "contextType": obj.get("contextType"),
            "institutionId": obj.get("institutionId"),
            "callback": obj.get("callback"),
            "redirect": RedirectRequest.from_dict(obj.get("redirect")) if obj.get("redirect") is not None else None,
            "oneTimeToken": obj.get("oneTimeToken"),
            "controlParameters": SweepingControlParameters.from_dict(obj.get("controlParameters")) if obj.get("controlParameters") is not None else None,
            "initiationDetails": InitiationDetails.from_dict(obj.get("initiationDetails")) if obj.get("initiationDetails") is not None else None
        })
        return _obj


