import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from yapily.models.account_request import AccountRequest
from yapily.models.redirect_request import RedirectRequest
from yapily.models.sca_method import ScaMethod
from yapily.models.user_credentials import UserCredentials


class EmbeddedAccountAuthorisationRequest(BaseModel):
    """
    EmbeddedAccountAuthorisationRequest
    """

    user_uuid: Annotated[
        StrictStr | None, Field(alias="userUuid", description="`User` for which the authorisation request was created.")
    ] = None
    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
        ),
    ] = None
    forward_parameters: Annotated[
        list[StrictStr] | None,
        Field(
            alias="forwardParameters",
            description="Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect.",
        ),
    ] = None
    institution_id: Annotated[
        StrictStr,
        Field(
            alias="institutionId",
            description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.",
        ),
    ]
    callback: Annotated[
        StrictStr | None,
        Field(
            description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/) for more information."
        ),
    ] = None
    redirect: RedirectRequest | None = None
    one_time_token: Annotated[
        StrictBool | None,
        Field(
            alias="oneTimeToken",
            description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.",
        ),
    ] = None
    user_credentials: Annotated[UserCredentials | None, Field(alias="userCredentials")] = None
    selected_sca_method: Annotated[ScaMethod | None, Field(alias="selectedScaMethod")] = None
    sca_code: Annotated[
        StrictStr | None,
        Field(
            alias="scaCode",
            description="__Conditional__. Used to update the authorisation with the sca code received by the user from the `Institution` using the embedded account authorisation flow.<br><br>This is the penultimate step required in the embedded account authorisation flow to authorise the `Consent`. After sending the sca code, to obtain an authorised consent, the last step is to poll [Get Consent](https://docs.yapily.com/api/reference/#operation/getConsentById) until the `Institution` authorises the request and the `Consent` `status` transitions to `AUTHORIZED`.",
        ),
    ] = None
    account_request: Annotated[AccountRequest | None, Field(alias="accountRequest")] = None
    __properties = [
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
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EmbeddedAccountAuthorisationRequest":
        """Create an instance of EmbeddedAccountAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
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
    def from_dict(cls, obj: dict) -> "EmbeddedAccountAuthorisationRequest":
        """Create an instance of EmbeddedAccountAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmbeddedAccountAuthorisationRequest.parse_obj(obj)

        return EmbeddedAccountAuthorisationRequest.parse_obj(
            {
                "user_uuid": obj.get("userUuid"),
                "application_user_id": obj.get("applicationUserId"),
                "forward_parameters": obj.get("forwardParameters"),
                "institution_id": obj.get("institutionId"),
                "callback": obj.get("callback"),
                "redirect": RedirectRequest.from_dict(obj.get("redirect")) if obj.get("redirect") is not None else None,
                "one_time_token": obj.get("oneTimeToken"),
                "user_credentials": UserCredentials.from_dict(obj.get("userCredentials"))
                if obj.get("userCredentials") is not None
                else None,
                "selected_sca_method": ScaMethod.from_dict(obj.get("selectedScaMethod"))
                if obj.get("selectedScaMethod") is not None
                else None,
                "sca_code": obj.get("scaCode"),
                "account_request": AccountRequest.from_dict(obj.get("accountRequest"))
                if obj.get("accountRequest") is not None
                else None,
            }
        )
