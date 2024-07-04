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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.hosted_payment_phase import HostedPaymentPhase
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails
from yapily.models.institution_identifiers_response import InstitutionIdentifiersResponse
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_type_response import PaymentTypeResponse

class HostedPayment(BaseModel):
    """
    HostedPayment
    """
    payment_id: Optional[StrictStr] = Field(None, alias="paymentId", description="The Unique Identifier of the payment.")
    hosted_payment_id: Optional[StrictStr] = Field(None, alias="hostedPaymentId", description="The Unique Identifier of the payment created using Yapily hosted application.")
    consent_id: Optional[StrictStr] = Field(None, alias="consentId", description="The Unique Identifier of the consent.")
    institution_identifiers: Optional[InstitutionIdentifiersResponse] = Field(None, alias="institutionIdentifiers")
    phases: Optional[conlist(HostedPaymentPhase)] = Field(None, description="The phase reached by the payment and its timestamp.")
    payment_status: Optional[StrictStr] = Field(None, alias="paymentStatus", description="Payment status based on latest HostedAuthPaymentPhase in phases. Value can be <ul> <li>PENDING  -  Payment pending processing</li> <li>COMPLETED  -  Payment processing completed</li> <li>FAILED  -  Payment process failed</li></ul>")
    status_details: Optional[conlist(HostedPaymentStatusDetails)] = Field(None, alias="statusDetails", description="Details of the payment status.")
    institution_payment_id: Optional[StrictStr] = Field(None, alias="institutionPaymentId", description="The Unique Identifier of the payment created with the `Institution`.")
    payment_lifecycle_id: Optional[StrictStr] = Field(None, alias="paymentLifecycleId", description="The Unique Identifier provided by TPP in the Payment request to identify the payment.")
    payment_idempotency_id: Optional[StrictStr] = Field(None, alias="paymentIdempotencyId", description="A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters.")
    reference: Optional[StrictStr] = Field(None, description="The payment reference or description. Limited to a maximum of 18 characters for UK institutions.")
    context_type: Optional[PaymentContextTypeResponse] = Field(None, alias="contextType")
    type: Optional[PaymentTypeResponse] = None
    payee: Optional[PayeeDetailsResponse] = None
    payer: Optional[PayerDetailsResponse] = None
    amount: Optional[AmountDetailsResponse] = None
    __properties = ["paymentId", "hostedPaymentId", "consentId", "institutionIdentifiers", "phases", "paymentStatus", "statusDetails", "institutionPaymentId", "paymentLifecycleId", "paymentIdempotencyId", "reference", "contextType", "type", "payee", "payer", "amount"]

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
    def from_json(cls, json_str: str) -> HostedPayment:
        """Create an instance of HostedPayment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phases (list)
        _items = []
        if self.phases:
            for _item in self.phases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['phases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in status_details (list)
        _items = []
        if self.status_details:
            for _item in self.status_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['statusDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict['payee'] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict['payer'] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HostedPayment:
        """Create an instance of HostedPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedPayment.parse_obj(obj)

        _obj = HostedPayment.parse_obj({
            "payment_id": obj.get("paymentId"),
            "hosted_payment_id": obj.get("hostedPaymentId"),
            "consent_id": obj.get("consentId"),
            "institution_identifiers": InstitutionIdentifiersResponse.from_dict(obj.get("institutionIdentifiers")) if obj.get("institutionIdentifiers") is not None else None,
            "phases": [HostedPaymentPhase.from_dict(_item) for _item in obj.get("phases")] if obj.get("phases") is not None else None,
            "payment_status": obj.get("paymentStatus"),
            "status_details": [HostedPaymentStatusDetails.from_dict(_item) for _item in obj.get("statusDetails")] if obj.get("statusDetails") is not None else None,
            "institution_payment_id": obj.get("institutionPaymentId"),
            "payment_lifecycle_id": obj.get("paymentLifecycleId"),
            "payment_idempotency_id": obj.get("paymentIdempotencyId"),
            "reference": obj.get("reference"),
            "context_type": obj.get("contextType"),
            "type": obj.get("type"),
            "payee": PayeeDetailsResponse.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
            "payer": PayerDetailsResponse.from_dict(obj.get("payer")) if obj.get("payer") is not None else None,
            "amount": AmountDetailsResponse.from_dict(obj.get("amount")) if obj.get("amount") is not None else None
        })
        return _obj


