import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr

from yapily.models.account_balance import AccountBalance
from yapily.models.account_identification import AccountIdentification
from yapily.models.account_name import AccountName
from yapily.models.account_type import AccountType
from yapily.models.consolidated_account_information import ConsolidatedAccountInformation
from yapily.models.usage_type import UsageType


class Account(BaseModel):
    """
    Account
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier of the account.")] = None
    type: Annotated[StrictStr | None, Field(description="Specifies the type of account e.g. (BUSINESS_CURRENT).")] = (
        None
    )
    description: Annotated[
        StrictStr | None, Field(description="Product name as defined by the financial institution for this account")
    ] = None
    balance: Annotated[
        StrictFloat | StrictInt | None,
        Field(
            description="Main / headline balance for the account. <br><br> Use of this field is recommended as fallback only. Instead, use of the typed balances (accountBalances) is recommended."
        ),
    ] = None
    currency: Annotated[
        StrictStr | None,
        Field(
            description="Currency the bank account balance is denoted in. <br><br> Specified as a 3-letter ISO 4217 currency code"
        ),
    ] = None
    usage_type: Annotated[UsageType | None, Field(alias="usageType")] = None
    account_type: Annotated[AccountType | None, Field(alias="accountType")] = None
    nickname: Annotated[
        StrictStr | None,
        Field(
            description="Nickname of the account that was provided by the account owner. <br><br> May be used to aid identification of the account."
        ),
    ] = None
    details: Annotated[
        StrictStr | None,
        Field(
            description="Supplementary specifications that might be provided by the Bank. These provide further characteristics about the account."
        ),
    ] = None
    account_names: Annotated[list[AccountName] | None, Field(alias="accountNames")] = None
    account_identifications: Annotated[list[AccountIdentification] | None, Field(alias="accountIdentifications")] = None
    account_balances: Annotated[list[AccountBalance] | None, Field(alias="accountBalances")] = None
    consolidated_account_information: Annotated[
        ConsolidatedAccountInformation | None, Field(alias="consolidatedAccountInformation")
    ] = None
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
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Account":
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
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
            _dict["consolidatedAccountInformation"] = self.consolidated_account_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "Account":
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Account.model_validate(obj)

        return Account.model_validate(
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
                "account_names": [AccountName.from_dict(_item) for _item in obj.get("accountNames")]
                if obj.get("accountNames") is not None
                else None,
                "account_identifications": [
                    AccountIdentification.from_dict(_item) for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
                "account_balances": [AccountBalance.from_dict(_item) for _item in obj.get("accountBalances")]
                if obj.get("accountBalances") is not None
                else None,
                "consolidated_account_information": ConsolidatedAccountInformation.from_dict(
                    obj.get("consolidatedAccountInformation")
                )
                if obj.get("consolidatedAccountInformation") is not None
                else None,
            }
        )
