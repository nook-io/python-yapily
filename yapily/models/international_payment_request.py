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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.charge_bearer_type import ChargeBearerType
from yapily.models.exchange_rate_information import ExchangeRateInformation
from yapily.models.priority_code_enum import PriorityCodeEnum
from typing import Set
from typing_extensions import Self


class InternationalPaymentRequest(BaseModel):
    """
    __Conditional__. Used to specify properties to define an international payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>INTERNATIONAL_SINGLE_PAYMENT</code></li>     <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>
    """  # noqa: E501

    currency_of_transfer: StrictStr = Field(
        description="__Mandatory__. The currency to be transferred to the payee. This may differ from the currency the payment is denoted in and the currency of the payer's account. Specified as a 3-letter code (ISO 4217).",
        alias="currencyOfTransfer",
    )
    exchange_rate_information: Optional[ExchangeRateInformation] = Field(
        default=None, alias="exchangeRateInformation"
    )
    purpose: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. Used to indicate the external purpose as a [ISO20022 purpose code](https://www.rba.hr/documents/20182/183267/External+purpose+codes+list/8a28f888-1f83-5e29-d6ed-fce05f428689?version=1.1) value.",
    )
    priority: Optional[PriorityCodeEnum] = None
    charge_bearer: Optional[ChargeBearerType] = Field(
        default=None, alias="chargeBearer"
    )
    __properties: ClassVar[List[str]] = [
        "currencyOfTransfer",
        "exchangeRateInformation",
        "purpose",
        "priority",
        "chargeBearer",
    ]

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
        """Create an instance of InternationalPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of exchange_rate_information
        if self.exchange_rate_information:
            _dict["exchangeRateInformation"] = self.exchange_rate_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InternationalPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "currencyOfTransfer": obj.get("currencyOfTransfer"),
                "exchangeRateInformation": ExchangeRateInformation.from_dict(
                    obj["exchangeRateInformation"]
                )
                if obj.get("exchangeRateInformation") is not None
                else None,
                "purpose": obj.get("purpose"),
                "priority": obj.get("priority"),
                "chargeBearer": obj.get("chargeBearer"),
            }
        )
        return _obj
