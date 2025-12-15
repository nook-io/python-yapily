from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.feature_enum import FeatureEnum
from yapily.models.sca_method import ScaMethod
from typing import Set
from typing_extensions import Self


class EmbeddedAccountAuthorisationResponse(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier for the embedded account authorisation request.",
    )
    user_uuid: Optional[StrictStr] = Field(
        default=None,
        description="The `User` that the authorisation request was created for.",
        alias="userUuid",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="The user-friendly reference to the `User` that the authorisation request was created for.",
        alias="applicationUserId",
    )
    reference_id: Optional[StrictStr] = Field(default=None, alias="referenceId")
    institution_id: Optional[StrictStr] = Field(
        default=None,
        description="The `Institution` the authorisation request was sent to.",
        alias="institutionId",
    )
    status: Optional[AuthorisationStatus] = None
    created_at: Optional[datetime] = Field(
        default=None,
        description="Date and time the embedded authorisation was created by the application user.",
        alias="createdAt",
    )
    transaction_from: Optional[datetime] = Field(
        default=None,
        description="When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved.",
        alias="transactionFrom",
    )
    transaction_to: Optional[datetime] = Field(
        default=None,
        description="When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved.",
        alias="transactionTo",
    )
    expires_at: Optional[datetime] = Field(
        default=None,
        description="Date and time the embedded authorisation expires. Re-authorisation is needed to retain access.",
        alias="expiresAt",
    )
    time_to_expire_in_millis: Optional[StrictInt] = Field(
        default=None, alias="timeToExpireInMillis"
    )
    time_to_expire: Optional[StrictStr] = Field(default=None, alias="timeToExpire")
    feature_scope: Optional[List[FeatureEnum]] = Field(
        default=None,
        description="The set of features the consent provides access to.",
        alias="featureScope",
    )
    consent_token: Optional[StrictStr] = Field(
        default=None,
        description="Represents the authorisation to gain access to the requested features. Required to access account information.",
        alias="consentToken",
    )
    state: Optional[StrictStr] = Field(
        default=None,
        description="Correlation ID used when handshaking with a new institution via OAuth2 registration.",
    )
    authorized_at: Optional[datetime] = Field(
        default=None,
        description="Date and time the request was authorised by the `Institution`.",
        alias="authorizedAt",
    )
    institution_consent_id: Optional[StrictStr] = Field(
        default=None,
        description="Identification of the consent at the `Institution`.",
        alias="institutionConsentId",
    )
    authorisation_url: Optional[StrictStr] = Field(
        default=None, alias="authorisationUrl"
    )
    qr_code_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL link for the QR code that may be scanned via a mobile device to make an authorisation redirect to the bank (authURL encoded).",
        alias="qrCodeUrl",
    )
    sca_methods: Optional[List[ScaMethod]] = Field(
        default=None,
        description="List of `SCA methods` that the `Institution` supports and are available for selection.",
        alias="scaMethods",
    )
    selected_sca_method: Optional[ScaMethod] = Field(
        default=None, alias="selectedScaMethod"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "userUuid",
        "applicationUserId",
        "referenceId",
        "institutionId",
        "status",
        "createdAt",
        "transactionFrom",
        "transactionTo",
        "expiresAt",
        "timeToExpireInMillis",
        "timeToExpire",
        "featureScope",
        "consentToken",
        "state",
        "authorizedAt",
        "institutionConsentId",
        "authorisationUrl",
        "qrCodeUrl",
        "scaMethods",
        "selectedScaMethod",
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
        _items = []
        if self.sca_methods:
            for _item_sca_methods in self.sca_methods:
                if _item_sca_methods:
                    _items.append(_item_sca_methods.to_dict())
            _dict["scaMethods"] = _items
        if self.selected_sca_method:
            _dict["selectedScaMethod"] = self.selected_sca_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "userUuid": obj.get("userUuid"),
                "applicationUserId": obj.get("applicationUserId"),
                "referenceId": obj.get("referenceId"),
                "institutionId": obj.get("institutionId"),
                "status": obj.get("status"),
                "createdAt": obj.get("createdAt"),
                "transactionFrom": obj.get("transactionFrom"),
                "transactionTo": obj.get("transactionTo"),
                "expiresAt": obj.get("expiresAt"),
                "timeToExpireInMillis": obj.get("timeToExpireInMillis"),
                "timeToExpire": obj.get("timeToExpire"),
                "featureScope": obj.get("featureScope"),
                "consentToken": obj.get("consentToken"),
                "state": obj.get("state"),
                "authorizedAt": obj.get("authorizedAt"),
                "institutionConsentId": obj.get("institutionConsentId"),
                "authorisationUrl": obj.get("authorisationUrl"),
                "qrCodeUrl": obj.get("qrCodeUrl"),
                "scaMethods": [
                    ScaMethod.from_dict(_item) for _item in obj["scaMethods"]
                ]
                if obj.get("scaMethods") is not None
                else None,
                "selectedScaMethod": ScaMethod.from_dict(obj["selectedScaMethod"])
                if obj.get("selectedScaMethod") is not None
                else None,
            }
        )
        return _obj
