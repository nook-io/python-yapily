from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.hosted_payment_request_details_link import (
    HostedPaymentRequestDetailsLink,
)
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.user_settings import UserSettings
from typing import Set
from typing_extensions import Self


class CreateHostedPaymentRequestLink(BaseModel):
    user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Yapily Identifier for the `User` returned by the create user step POST /users. You must either provide `userId` or `applicationUserId`.",
        alias="userId",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. Your own `User` reference. If you want to work with their own unique references for individual PSUs then you can use the `applicationUserId` property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied `applicationUserId`, then a new Yapily userId is created automatically and linked to the `applicationUserId` value. You must either provide userId or `applicationUserId`.",
        alias="applicationUserId",
    )
    institution_identifiers: InstitutionIdentifiers = Field(
        alias="institutionIdentifiers"
    )
    user_settings: Optional[UserSettings] = Field(default=None, alias="userSettings")
    redirect_url: StrictStr = Field(
        description="URL of your server to redirect the user after completion of the payment flow.",
        alias="redirectUrl",
    )
    authorisation_expires_at: Optional[datetime] = Field(
        default=None,
        description="The date and time that the authorisation expires. Must be between 10 minutes and 30 days in the future. If not specified, the authorisation URL will expire 10 minutes after creation.",
        alias="authorisationExpiresAt",
    )
    payment_request_details: HostedPaymentRequestDetailsLink = Field(
        alias="paymentRequestDetails"
    )
    __properties: ClassVar[List[str]] = [
        "userId",
        "applicationUserId",
        "institutionIdentifiers",
        "userSettings",
        "redirectUrl",
        "authorisationExpiresAt",
        "paymentRequestDetails",
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
        if self.institution_identifiers:
            _dict["institutionIdentifiers"] = self.institution_identifiers.to_dict()
        if self.user_settings:
            _dict["userSettings"] = self.user_settings.to_dict()
        if self.payment_request_details:
            _dict["paymentRequestDetails"] = self.payment_request_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "userId": obj.get("userId"),
                "applicationUserId": obj.get("applicationUserId"),
                "institutionIdentifiers": InstitutionIdentifiers.from_dict(
                    obj["institutionIdentifiers"]
                )
                if obj.get("institutionIdentifiers") is not None
                else None,
                "userSettings": UserSettings.from_dict(obj["userSettings"])
                if obj.get("userSettings") is not None
                else None,
                "redirectUrl": obj.get("redirectUrl"),
                "authorisationExpiresAt": obj.get("authorisationExpiresAt"),
                "paymentRequestDetails": HostedPaymentRequestDetailsLink.from_dict(
                    obj["paymentRequestDetails"]
                )
                if obj.get("paymentRequestDetails") is not None
                else None,
            }
        )
        return _obj
