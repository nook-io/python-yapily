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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.exchange_rate_information_response import ExchangeRateInformationResponse
from yapily.models.feature_enum import FeatureEnum
from yapily.models.payment_charge_details import PaymentChargeDetails
from yapily.models.sca_method import ScaMethod
from typing import Optional, Set
from typing_extensions import Self

class PaymentEmbeddedAuthorisationRequestResponse(BaseModel):
    """
    PaymentEmbeddedAuthorisationRequestResponse
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the embedded payment authorisation request.")
    user_uuid: Optional[StrictStr] = Field(default=None, description="The `User` that the authorisation request was created for.", alias="userUuid")
    application_user_id: Optional[StrictStr] = Field(default=None, description="The user-friendly reference to the `User` that the authorisation request was created for.", alias="applicationUserId")
    reference_id: Optional[StrictStr] = Field(default=None, alias="referenceId")
    institution_id: Optional[StrictStr] = Field(default=None, description="The  `Institution` the authorisation request was sent to.", alias="institutionId")
    status: Optional[AuthorisationStatus] = None
    created_at: Optional[datetime] = Field(default=None, description="Date and time the embedded payment authorisation was created.", alias="createdAt")
    transaction_from: Optional[datetime] = Field(default=None, description="When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved.", alias="transactionFrom")
    transaction_to: Optional[datetime] = Field(default=None, description="When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved.", alias="transactionTo")
    expires_at: Optional[datetime] = Field(default=None, description="Date and time the authorisation expires. Re-authorisation is needed to retain access.", alias="expiresAt")
    time_to_expire_in_millis: Optional[StrictInt] = Field(default=None, alias="timeToExpireInMillis")
    time_to_expire: Optional[StrictStr] = Field(default=None, alias="timeToExpire")
    feature_scope: Optional[List[FeatureEnum]] = Field(default=None, description="The set of features the consent provides access to.", alias="featureScope")
    consent_token: Optional[StrictStr] = Field(default=None, description="Represents the authorisation to gain access to the requested features. Required to make a payment request.", alias="consentToken")
    state: Optional[StrictStr] = Field(default=None, description="Correlation ID used with the `Institution` during the authorisation process.")
    authorized_at: Optional[datetime] = Field(default=None, description="Date and time the request was authorised by the `Institution`.", alias="authorizedAt")
    institution_consent_id: Optional[StrictStr] = Field(default=None, description="Identification of the consent at the `Institution`.", alias="institutionConsentId")
    charges: Optional[List[PaymentChargeDetails]] = None
    exchange_rate_information: Optional[ExchangeRateInformationResponse] = Field(default=None, alias="exchangeRateInformation")
    authorisation_url: Optional[StrictStr] = Field(default=None, alias="authorisationUrl")
    qr_code_url: Optional[StrictStr] = Field(default=None, description="The URL link for the QR code that may be scanned via a mobile device to make an authorisation redirect to the bank (authURL encoded).", alias="qrCodeUrl")
    explanation: Optional[StrictStr] = None
    sca_methods: Optional[List[ScaMethod]] = Field(default=None, alias="scaMethods")
    selected_sca_method: Optional[ScaMethod] = Field(default=None, alias="selectedScaMethod")
    __properties: ClassVar[List[str]] = ["id", "userUuid", "applicationUserId", "referenceId", "institutionId", "status", "createdAt", "transactionFrom", "transactionTo", "expiresAt", "timeToExpireInMillis", "timeToExpire", "featureScope", "consentToken", "state", "authorizedAt", "institutionConsentId", "charges", "exchangeRateInformation", "authorisationUrl", "qrCodeUrl", "explanation", "scaMethods", "selectedScaMethod"]

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
        """Create an instance of PaymentEmbeddedAuthorisationRequestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item_charges in self.charges:
                if _item_charges:
                    _items.append(_item_charges.to_dict())
            _dict['charges'] = _items
        # override the default output from pydantic by calling `to_dict()` of exchange_rate_information
        if self.exchange_rate_information:
            _dict['exchangeRateInformation'] = self.exchange_rate_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sca_methods (list)
        _items = []
        if self.sca_methods:
            for _item_sca_methods in self.sca_methods:
                if _item_sca_methods:
                    _items.append(_item_sca_methods.to_dict())
            _dict['scaMethods'] = _items
        # override the default output from pydantic by calling `to_dict()` of selected_sca_method
        if self.selected_sca_method:
            _dict['selectedScaMethod'] = self.selected_sca_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentEmbeddedAuthorisationRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
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
            "charges": [PaymentChargeDetails.from_dict(_item) for _item in obj["charges"]] if obj.get("charges") is not None else None,
            "exchangeRateInformation": ExchangeRateInformationResponse.from_dict(obj["exchangeRateInformation"]) if obj.get("exchangeRateInformation") is not None else None,
            "authorisationUrl": obj.get("authorisationUrl"),
            "qrCodeUrl": obj.get("qrCodeUrl"),
            "explanation": obj.get("explanation"),
            "scaMethods": [ScaMethod.from_dict(_item) for _item in obj["scaMethods"]] if obj.get("scaMethods") is not None else None,
            "selectedScaMethod": ScaMethod.from_dict(obj["selectedScaMethod"]) if obj.get("selectedScaMethod") is not None else None
        })
        return _obj


