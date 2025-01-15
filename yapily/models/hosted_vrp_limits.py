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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.amount import Amount
from yapily.models.hosted_non_sweeping_periodic_limits import (
    HostedNonSweepingPeriodicLimits,
)
from typing import Set
from typing_extensions import Self


class HostedVRPLimits(BaseModel):
    """
    The restrictions and limits for payments executed under the VRP consent
    """  # noqa: E501

    periodic_limits: Optional[List[HostedNonSweepingPeriodicLimits]] = Field(
        default=None, alias="periodicLimits"
    )
    max_amount_per_payment: Optional[Amount] = Field(
        default=None,
        description="__Optional__. Max amount that can be submitted per payment.",
        alias="maxAmountPerPayment",
    )
    max_cumulative_amount: Optional[Amount] = Field(
        default=None,
        description="__Optional__. Max cumulative amount that can be submitted under this consent.",
        alias="maxCumulativeAmount",
    )
    max_cumulative_number_of_payments: Optional[StrictInt] = Field(
        default=None,
        description="__Optional__. Max number of payments that can be submitted under this consent.",
        alias="maxCumulativeNumberOfPayments",
    )
    edited_by_user: Optional[StrictBool] = Field(
        default=None,
        description="Indicates if the user edited the control parameters during authorisation",
        alias="editedByUser",
    )
    __properties: ClassVar[List[str]] = [
        "periodicLimits",
        "maxAmountPerPayment",
        "maxCumulativeAmount",
        "maxCumulativeNumberOfPayments",
        "editedByUser",
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
        """Create an instance of HostedVRPLimits from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in periodic_limits (list)
        _items = []
        if self.periodic_limits:
            for _item_periodic_limits in self.periodic_limits:
                if _item_periodic_limits:
                    _items.append(_item_periodic_limits.to_dict())
            _dict["periodicLimits"] = _items
        # override the default output from pydantic by calling `to_dict()` of max_amount_per_payment
        if self.max_amount_per_payment:
            _dict["maxAmountPerPayment"] = self.max_amount_per_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_cumulative_amount
        if self.max_cumulative_amount:
            _dict["maxCumulativeAmount"] = self.max_cumulative_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostedVRPLimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "periodicLimits": [
                    HostedNonSweepingPeriodicLimits.from_dict(_item)
                    for _item in obj["periodicLimits"]
                ]
                if obj.get("periodicLimits") is not None
                else None,
                "maxAmountPerPayment": Amount.from_dict(obj["maxAmountPerPayment"])
                if obj.get("maxAmountPerPayment") is not None
                else None,
                "maxCumulativeAmount": Amount.from_dict(obj["maxCumulativeAmount"])
                if obj.get("maxCumulativeAmount") is not None
                else None,
                "maxCumulativeNumberOfPayments": obj.get(
                    "maxCumulativeNumberOfPayments"
                ),
                "editedByUser": obj.get("editedByUser"),
            }
        )
        return _obj
