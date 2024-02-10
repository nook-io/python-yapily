# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from yapily.models.virtual_account_payment_amount import VirtualAccountPaymentAmount
from yapily.models.virtual_account_payment_source import VirtualAccountPaymentSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualAccountPayInDetails(BaseModel):
    """
    VirtualAccountPayInDetails
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique id of the payment")
    payment_scheme: Optional[StrictStr] = Field(default=None, description="Method of settlement to complete the payment. One of: <br> FASTER_PAYMENTS <br> SEPA_CREDIT <br> SEPA_INSTANT <br> SWIFT <br> SWIFT_EXPRESS <br> CHAPS <br> IAT <br> WIRE", alias="paymentScheme")
    amount: Optional[VirtualAccountPaymentAmount] = None
    reference: Optional[StrictStr] = Field(default=None, description="Reference associated with the payment and which appears on the beneficiary's bank statement")
    source: Optional[VirtualAccountPaymentSource] = None
    name: Optional[StrictStr] = Field(default=None, description="Account source name")
    address: Optional[StrictStr] = Field(default=None, description="The address of the source bank account")
    __properties: ClassVar[List[str]] = ["id", "paymentScheme", "amount", "reference", "source", "name", "address"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualAccountPayInDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VirtualAccountPayInDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "paymentScheme": obj.get("paymentScheme"),
            "amount": VirtualAccountPaymentAmount.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "reference": obj.get("reference"),
            "source": VirtualAccountPaymentSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "name": obj.get("name"),
            "address": obj.get("address")
        })
        return _obj


