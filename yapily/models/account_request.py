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
from typing import Optional
from pydantic import BaseModel, Field, conlist
from yapily.models.account_info import AccountInfo
from yapily.models.feature_enum import FeatureEnum


class AccountRequest(BaseModel):
    """
    __Conditional__. Used to further specify details of the `Consent` to request <br><br>Conditions:<ol><li>Mandatory to specify the individual scopes to request from the user at the `Institution` for an account authorisation</li><li>Mandatory to specify an expiry time on the created `Consent` at which time will render it unusable</li><li>Mandatory to specify the date range that the created `Consent` will be able to access transactions for (given the range is support for the `Institution`)</li></ol>  # noqa: E501
    """

    transaction_from: Optional[datetime] = Field(
        default=None,
        alias="transactionFrom",
        description="__Optional__. Specifies the earliest date of the transaction records to be returned.<br><br> You must supply this field to retrieve transactions older than 90 days for banks accessed via the the [CBI Globe Gateway](https://docs.yapily.com/pages/data/financial-data-resources/data-restrictions/#cbi-globe-gateway).",
    )
    transaction_to: Optional[datetime] = Field(
        default=None,
        alias="transactionTo",
        description="__Optional__. Specifies the latest date of the transaction records to be returned.",
    )
    expires_at: Optional[datetime] = Field(
        default=None,
        alias="expiresAt",
        description="__Optional__. Used to set a hard date for when the user's associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every `Institution`. In such case, the request will not fail but the property will be ignored and the created `Consent` will not have an expiry date.",
    )
    account_identifiers: Optional[AccountInfo] = Field(
        default=None, alias="accountIdentifiers"
    )
    account_identifiers_for_transaction: Optional[conlist(AccountInfo)] = Field(
        default=None,
        alias="accountIdentifiersForTransaction",
        description="__Conditional__. Used to create a request for the transactions of the account specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and transactions.",
    )
    account_identifiers_for_balance: Optional[conlist(AccountInfo)] = Field(
        default=None,
        alias="accountIdentifiersForBalance",
        description="__Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.",
    )
    feature_scope: Optional[conlist(FeatureEnum, unique_items=True)] = Field(
        default=None,
        alias="featureScope",
        description="__Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).",
    )
    __properties = [
        "transactionFrom",
        "transactionTo",
        "expiresAt",
        "accountIdentifiers",
        "accountIdentifiersForTransaction",
        "accountIdentifiersForBalance",
        "featureScope",
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
    def from_json(cls, json_str: str) -> AccountRequest:
        """Create an instance of AccountRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account_identifiers
        if self.account_identifiers:
            _dict["accountIdentifiers"] = self.account_identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifiers_for_transaction (list)
        _items = []
        if self.account_identifiers_for_transaction:
            for _item in self.account_identifiers_for_transaction:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountIdentifiersForTransaction"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifiers_for_balance (list)
        _items = []
        if self.account_identifiers_for_balance:
            for _item in self.account_identifiers_for_balance:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountIdentifiersForBalance"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountRequest:
        """Create an instance of AccountRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountRequest.parse_obj(obj)

        _obj = AccountRequest.parse_obj(
            {
                "transaction_from": obj.get("transactionFrom"),
                "transaction_to": obj.get("transactionTo"),
                "expires_at": obj.get("expiresAt"),
                "account_identifiers": AccountInfo.from_dict(
                    obj.get("accountIdentifiers")
                )
                if obj.get("accountIdentifiers") is not None
                else None,
                "account_identifiers_for_transaction": [
                    AccountInfo.from_dict(_item)
                    for _item in obj.get("accountIdentifiersForTransaction")
                ]
                if obj.get("accountIdentifiersForTransaction") is not None
                else None,
                "account_identifiers_for_balance": [
                    AccountInfo.from_dict(_item)
                    for _item in obj.get("accountIdentifiersForBalance")
                ]
                if obj.get("accountIdentifiersForBalance") is not None
                else None,
                "feature_scope": obj.get("featureScope"),
            }
        )
        return _obj
