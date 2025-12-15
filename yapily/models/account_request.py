from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.account_info import AccountInfo
from yapily.models.feature_enum import FeatureEnum
from typing import Set
from typing_extensions import Self


class AccountRequest(BaseModel):
    transaction_from: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Specifies the earliest date of the transaction records to be returned.<br><br> You must supply this field to retrieve transactions older than 90 days for banks accessed via the the [CBI Globe Gateway](https://docs.yapily.com/pages/data/financial-data-resources/data-restrictions/#cbi-globe-gateway).",
        alias="transactionFrom",
    )
    transaction_to: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Specifies the latest date of the transaction records to be returned.",
        alias="transactionTo",
    )
    expires_at: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Used to set a hard date for when the user's associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every `Institution`. In such case, the request will not fail but the property will be ignored and the created `Consent` will not have an expiry date.",
        alias="expiresAt",
    )
    account_identifiers: Optional[AccountInfo] = Field(
        default=None, alias="accountIdentifiers"
    )
    account_identifiers_for_transaction: Optional[List[AccountInfo]] = Field(
        default=None,
        description="__Conditional__. Used to create a request for the transactions of the account specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and transactions.",
        alias="accountIdentifiersForTransaction",
    )
    account_identifiers_for_balance: Optional[List[AccountInfo]] = Field(
        default=None,
        description="__Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.",
        alias="accountIdentifiersForBalance",
    )
    feature_scope: Optional[List[FeatureEnum]] = Field(
        default=None,
        description="__Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).",
        alias="featureScope",
    )
    __properties: ClassVar[List[str]] = [
        "transactionFrom",
        "transactionTo",
        "expiresAt",
        "accountIdentifiers",
        "accountIdentifiersForTransaction",
        "accountIdentifiersForBalance",
        "featureScope",
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
        if self.account_identifiers:
            _dict["accountIdentifiers"] = self.account_identifiers.to_dict()
        _items = []
        if self.account_identifiers_for_transaction:
            for (
                _item_account_identifiers_for_transaction
            ) in self.account_identifiers_for_transaction:
                if _item_account_identifiers_for_transaction:
                    _items.append(_item_account_identifiers_for_transaction.to_dict())
            _dict["accountIdentifiersForTransaction"] = _items
        _items = []
        if self.account_identifiers_for_balance:
            for (
                _item_account_identifiers_for_balance
            ) in self.account_identifiers_for_balance:
                if _item_account_identifiers_for_balance:
                    _items.append(_item_account_identifiers_for_balance.to_dict())
            _dict["accountIdentifiersForBalance"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "transactionFrom": obj.get("transactionFrom"),
                "transactionTo": obj.get("transactionTo"),
                "expiresAt": obj.get("expiresAt"),
                "accountIdentifiers": AccountInfo.from_dict(obj["accountIdentifiers"])
                if obj.get("accountIdentifiers") is not None
                else None,
                "accountIdentifiersForTransaction": [
                    AccountInfo.from_dict(_item)
                    for _item in obj["accountIdentifiersForTransaction"]
                ]
                if obj.get("accountIdentifiersForTransaction") is not None
                else None,
                "accountIdentifiersForBalance": [
                    AccountInfo.from_dict(_item)
                    for _item in obj["accountIdentifiersForBalance"]
                ]
                if obj.get("accountIdentifiersForBalance") is not None
                else None,
                "featureScope": obj.get("featureScope"),
            }
        )
        return _obj
