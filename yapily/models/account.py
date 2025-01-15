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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from yapily.models.account_balance import AccountBalance
from yapily.models.account_identification import AccountIdentification
from yapily.models.account_name import AccountName
from yapily.models.account_type import AccountType
from yapily.models.consolidated_account_information import (
    ConsolidatedAccountInformation,
)
from yapily.models.usage_type import UsageType


class Account(BaseModel):
    """
    Account
    """

    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the account."
    )
    type: Optional[StrictStr] = Field(
        default=None,
        description="Specifies the type of account e.g. (BUSINESS_CURRENT).",
    )
    description: Optional[StrictStr] = Field(
        default=None,
        description="Product name as defined by the financial institution for this account",
    )
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Main / headline balance for the account. <br><br> Use of this field is recommended as fallback only. Instead, use of the typed balances (accountBalances) is recommended.",
    )
    currency: Optional[StrictStr] = Field(
        default=None,
        description="Currency the bank account balance is denoted in. <br><br> Specified as a 3-letter ISO 4217 currency code",
    )
    usage_type: Optional[UsageType] = Field(default=None, alias="usageType")
    account_type: Optional[AccountType] = Field(default=None, alias="accountType")
    nickname: Optional[StrictStr] = Field(
        default=None,
        description="Nickname of the account that was provided by the account owner. <br><br> May be used to aid identification of the account.",
    )
    details: Optional[StrictStr] = Field(
        default=None,
        description="Supplementary specifications that might be provided by the Bank. These provide further characteristics about the account.",
    )
    account_names: Optional[conlist(AccountName)] = Field(
        default=None, alias="accountNames"
    )
    account_identifications: Optional[
        conlist(AccountIdentification, unique_items=True)
    ] = Field(default=None, alias="accountIdentifications")
    account_balances: Optional[conlist(AccountBalance)] = Field(
        default=None, alias="accountBalances"
    )
    consolidated_account_information: Optional[ConsolidatedAccountInformation] = Field(
        default=None, alias="consolidatedAccountInformation"
    )
    __properties = [
        "id",
        "type",
        "description",
        "balance",
        "currency",
        "usageType",
        "accountType",
        "nickname",
        "details",
        "accountNames",
        "accountIdentifications",
        "accountBalances",
        "consolidatedAccountInformation",
    ]

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
    def from_json(cls, json_str: str) -> Account:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in account_names (list)
        _items = []
        if self.account_names:
            for _item in self.account_names:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountNames"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifications (list)
        _items = []
        if self.account_identifications:
            for _item in self.account_identifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountIdentifications"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_balances (list)
        _items = []
        if self.account_balances:
            for _item in self.account_balances:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountBalances"] = _items
        # override the default output from pydantic by calling `to_dict()` of consolidated_account_information
        if self.consolidated_account_information:
            _dict["consolidatedAccountInformation"] = (
                self.consolidated_account_information.to_dict()
            )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Account:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Account.parse_obj(obj)

        _obj = Account.parse_obj(
            {
                "id": obj.get("id"),
                "type": obj.get("type"),
                "description": obj.get("description"),
                "balance": obj.get("balance"),
                "currency": obj.get("currency"),
                "usage_type": obj.get("usageType"),
                "account_type": obj.get("accountType"),
                "nickname": obj.get("nickname"),
                "details": obj.get("details"),
                "account_names": [
                    AccountName.from_dict(_item) for _item in obj.get("accountNames")
                ]
                if obj.get("accountNames") is not None
                else None,
                "account_identifications": [
                    AccountIdentification.from_dict(_item)
                    for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
                "account_balances": [
                    AccountBalance.from_dict(_item)
                    for _item in obj.get("accountBalances")
                ]
                if obj.get("accountBalances") is not None
                else None,
                "consolidated_account_information": ConsolidatedAccountInformation.from_dict(
                    obj.get("consolidatedAccountInformation")
                )
                if obj.get("consolidatedAccountInformation") is not None
                else None,
            }
        )
        return _obj
