import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from yapily.models.payment_request import PaymentRequest
from yapily.models.redirect_request import RedirectRequest


class PaymentAuthorisationRequest(BaseModel):
    """
    The request body containing an `PaymentAuthorisationRequest` json payload  # noqa: E501
    """

    user_uuid: Annotated[StrictStr | None, Field(alias="userUuid")] = None
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
            description="__Optional__. The URL to redirect the user to after the user complete the authorisation at the `Institution`."
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
    payment_request: Annotated[PaymentRequest, Field(alias="paymentRequest")]
    __properties = [
        "userUuid",
        "applicationUserId",
        "forwardParameters",
        "institutionId",
        "callback",
        "redirect",
        "oneTimeToken",
        "paymentRequest",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentAuthorisationRequest":
        """Create an instance of PaymentAuthorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of redirect
        if self.redirect:
            _dict["redirect"] = self.redirect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_request
        if self.payment_request:
            _dict["paymentRequest"] = self.payment_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "PaymentAuthorisationRequest":
        """Create an instance of PaymentAuthorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentAuthorisationRequest.model_validate(obj)

        return PaymentAuthorisationRequest.model_validate(
            {
                "user_uuid": obj.get("userUuid"),
                "application_user_id": obj.get("applicationUserId"),
                "forward_parameters": obj.get("forwardParameters"),
                "institution_id": obj.get("institutionId"),
                "callback": obj.get("callback"),
                "redirect": RedirectRequest.from_dict(obj.get("redirect")) if obj.get("redirect") is not None else None,
                "one_time_token": obj.get("oneTimeToken"),
                "payment_request": PaymentRequest.from_dict(obj.get("paymentRequest"))
                if obj.get("paymentRequest") is not None
                else None,
            }
        )
