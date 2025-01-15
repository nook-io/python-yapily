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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.direct_debit_payee import DirectDebitPayee
from yapily.models.payment_status_details import PaymentStatusDetails
from typing import Optional, Set
from typing_extensions import Self

class DirectDebitResponse(BaseModel):
    """
    DirectDebitResponse
    """ # noqa: E501
    id: Optional[StrictStr] = None
    status_details: Optional[PaymentStatusDetails] = Field(default=None, alias="statusDetails")
    payee_details: Optional[DirectDebitPayee] = Field(default=None, alias="payeeDetails")
    reference: Optional[StrictStr] = None
    previous_payment_amount: Optional[Amount] = Field(default=None, alias="previousPaymentAmount")
    previous_payment_date_time: Optional[datetime] = Field(default=None, alias="previousPaymentDateTime")
    __properties: ClassVar[List[str]] = ["id", "statusDetails", "payeeDetails", "reference", "previousPaymentAmount", "previousPaymentDateTime"]

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
        """Create an instance of DirectDebitResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status_details
        if self.status_details:
            _dict['statusDetails'] = self.status_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payee_details
        if self.payee_details:
            _dict['payeeDetails'] = self.payee_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_payment_amount
        if self.previous_payment_amount:
            _dict['previousPaymentAmount'] = self.previous_payment_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DirectDebitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "statusDetails": PaymentStatusDetails.from_dict(obj["statusDetails"]) if obj.get("statusDetails") is not None else None,
            "payeeDetails": DirectDebitPayee.from_dict(obj["payeeDetails"]) if obj.get("payeeDetails") is not None else None,
            "reference": obj.get("reference"),
            "previousPaymentAmount": Amount.from_dict(obj["previousPaymentAmount"]) if obj.get("previousPaymentAmount") is not None else None,
            "previousPaymentDateTime": obj.get("previousPaymentDateTime")
        })
        return _obj


