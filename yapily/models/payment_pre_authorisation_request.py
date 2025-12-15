from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.payee_details import PayeeDetails
from yapily.models.payer_details import PayerDetails
from yapily.models.redirect_request import RedirectRequest
from typing import Set
from typing_extensions import Self


class PaymentPreAuthorisationRequest(BaseModel):
    user_uuid: Optional[StrictStr] = Field(default=None, alias="userUuid")
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. The user-friendly reference to the `User` that will authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
        alias="applicationUserId",
    )
    forward_parameters: Optional[List[StrictStr]] = Field(
        default=None,
        description="Extra parameters to be forwarded in the redirect back to the client after the user authorisation flow has been completed.",
        alias="forwardParameters",
    )
    institution_id: StrictStr = Field(
        description="__Mandatory__. The reference to the `Institution` which identifies which institution the authorisation request is sent to.",
        alias="institutionId",
    )
    callback: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for more information.",
    )
    redirect: Optional[RedirectRequest] = None
    one_time_token: Optional[StrictBool] = Field(
        default=None,
        description="__Conditional__. Used to receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set. <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.",
        alias="oneTimeToken",
    )
    scope: StrictStr = Field(
        description="__Mandatory__. Defines the scope of the pre-authorisation request."
    )
    payee: PayeeDetails
    payer: PayerDetails
    amount: Amount
    reference: StrictStr = Field(
        description="__Mandatory__. The payment reference or description. Limited to a maximum of 18 characters long."
    )
    __properties: ClassVar[List[str]] = [
        "userUuid",
        "applicationUserId",
        "forwardParameters",
        "institutionId",
        "callback",
        "redirect",
        "oneTimeToken",
        "scope",
        "payee",
        "payer",
        "amount",
        "reference",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.redirect:
            _dict["redirect"] = self.redirect.to_dict()
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        if self.amount:
            _dict["amount"] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
                "scope": obj.get("scope"),
                "payee": PayeeDetails.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "payer": PayerDetails.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "amount": Amount.from_dict(obj["amount"])
                if obj.get("amount") is not None
                else None,
                "reference": obj.get("reference"),
            }
        )
        return _obj
