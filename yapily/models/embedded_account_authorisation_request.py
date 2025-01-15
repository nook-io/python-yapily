# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_request import AccountRequest
from yapily.models.redirect_request import RedirectRequest
from yapily.models.sca_method import ScaMethod
from yapily.models.user_credentials import UserCredentials
from typing import Set
from typing_extensions import Self


class EmbeddedAccountAuthorisationRequest(BaseModel):
    """
    EmbeddedAccountAuthorisationRequest
    """  # noqa: E501

    user_uuid: Optional[StrictStr] = Field(
        default=None,
        description="`User` for which the authorisation request was created.",
        alias="userUuid",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
        alias="applicationUserId",
    )
    forward_parameters: Optional[List[StrictStr]] = Field(
        default=None,
        description="Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect.",
        alias="forwardParameters",
    )
    institution_id: StrictStr = Field(
        description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.",
        alias="institutionId",
    )
    callback: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/) for more information.",
    )
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(
        default=None,
        description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.",
        alias="oneTimeToken",
    )
    user_credentials: Optional[UserCredentials] = Field(
        default=None, alias="userCredentials"
    )
    selected_sca_method: Optional[ScaMethod] = Field(
        default=None, alias="selectedScaMethod"
    )
    sca_code: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Used to update the authorisation with the sca code received by the user from the `Institution` using the embedded account authorisation flow.<br><br>This is the penultimate step required in the embedded account authorisation flow to authorise the `Consent`. After sending the sca code, to obtain an authorised consent, the last step is to poll [Get Consent](https://docs.yapily.com/api/reference/#operation/getConsentById) until the `Institution` authorises the request and the `Consent` `status` transitions to `AUTHORIZED`.",
        alias="scaCode",
    )
    account_request: Optional[AccountRequest] = Field(
        default=None, alias="accountRequest"
    )
    __properties: ClassVar[List[str]] = [
        "userUuid",
        "applicationUserId",
        "forwardParameters",
        "institutionId",
        "callback",
        "redirect",
        "oneTimeToken",
        "userCredentials",
        "selectedScaMethod",
        "scaCode",
        "accountRequest",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EmbeddedAccountAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of redirect
        if self.redirect:
            _dict["redirect"] = self.redirect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_credentials
        if self.user_credentials:
            _dict["userCredentials"] = self.user_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selected_sca_method
        if self.selected_sca_method:
            _dict["selectedScaMethod"] = self.selected_sca_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_request
        if self.account_request:
            _dict["accountRequest"] = self.account_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmbeddedAccountAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "userUuid": obj.get("userUuid"),
                "applicationUserId": obj.get("applicationUserId"),
                "forwardParameters": obj.get("forwardParameters"),
                "institutionId": obj.get("institutionId"),
                "callback": obj.get("callback"),
                "redirect": RedirectRequest.from_dict(obj["redirect"])
                if obj.get("redirect") is not None
                else None,
                "oneTimeToken": obj.get("oneTimeToken"),
                "userCredentials": UserCredentials.from_dict(obj["userCredentials"])
                if obj.get("userCredentials") is not None
                else None,
                "selectedScaMethod": ScaMethod.from_dict(obj["selectedScaMethod"])
                if obj.get("selectedScaMethod") is not None
                else None,
                "scaCode": obj.get("scaCode"),
                "accountRequest": AccountRequest.from_dict(obj["accountRequest"])
                if obj.get("accountRequest") is not None
                else None,
            }
        )
        return _obj
