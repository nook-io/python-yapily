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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_type_response import PaymentTypeResponse
from typing import Optional, Set
from typing_extensions import Self

class HostedPaymentRequestDetailsLink(BaseModel):
    """
    HostedPaymentRequestDetailsLink
    """ # noqa: E501
    reference: Optional[StrictStr] = Field(default=None, description="The payment reference or description. Limited to a maximum of 18 characters for UK institutions.")
    context_type: Optional[PaymentContextTypeResponse] = Field(default=None, alias="contextType")
    type: Optional[PaymentTypeResponse] = None
    payee: Optional[PayeeDetailsResponse] = None
    payer: Optional[PayerDetailsResponse] = None
    amount_details: Optional[AmountDetailsResponse] = Field(default=None, alias="amountDetails")
    payment_due_date: Optional[date] = Field(default=None, description="The date that the payment is due. Displayed to the end user in the payment summary screen.", alias="paymentDueDate")
    __properties: ClassVar[List[str]] = ["reference", "contextType", "type", "payee", "payer", "amountDetails", "paymentDueDate"]

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
        """Create an instance of HostedPaymentRequestDetailsLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict['payee'] = self.payee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict['payer'] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_details
        if self.amount_details:
            _dict['amountDetails'] = self.amount_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostedPaymentRequestDetailsLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "contextType": obj.get("contextType"),
            "type": obj.get("type"),
            "payee": PayeeDetailsResponse.from_dict(obj["payee"]) if obj.get("payee") is not None else None,
            "payer": PayerDetailsResponse.from_dict(obj["payer"]) if obj.get("payer") is not None else None,
            "amountDetails": AmountDetailsResponse.from_dict(obj["amountDetails"]) if obj.get("amountDetails") is not None else None,
            "paymentDueDate": obj.get("paymentDueDate")
        })
        return _obj


