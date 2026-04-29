import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool

from yapily.models.account_balance_type import AccountBalanceType
from yapily.models.amount import Amount
from yapily.models.credit_line import CreditLine


class AccountBalance(BaseModel):
    """
    AccountBalance
    """

    type: AccountBalanceType | None = None
    date_time: Annotated[
        datetime | None, Field(alias="dateTime", description="Date and time of the reported balance.")
    ] = None
    balance_amount: Annotated[Amount | None, Field(alias="balanceAmount")] = None
    credit_line_included: Annotated[
        StrictBool | None,
        Field(
            alias="creditLineIncluded",
            description="_Optional_. Indicates whether any credit lines are included in the balance.",
        ),
    ] = None
    credit_lines: Annotated[
        list[CreditLine] | None, Field(alias="creditLines", description="_Optional_. Specifies the type of balance.")
    ] = None
    __properties = ["type", "dateTime", "balanceAmount", "creditLineIncluded", "creditLines"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AccountBalance":
        """Create an instance of AccountBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of balance_amount
        if self.balance_amount:
            _dict["balanceAmount"] = self.balance_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in credit_lines (list)
        _items = []
        if self.credit_lines:
            for _item in self.credit_lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict["creditLines"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "AccountBalance":
        """Create an instance of AccountBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountBalance.model_validate(obj)

        return AccountBalance.model_validate(
            {
                "type": obj.get("type"),
                "date_time": obj.get("dateTime"),
                "balance_amount": Amount.from_dict(obj.get("balanceAmount"))
                if obj.get("balanceAmount") is not None
                else None,
                "credit_line_included": obj.get("creditLineIncluded"),
                "credit_lines": [CreditLine.from_dict(_item) for _item in obj.get("creditLines")]
                if obj.get("creditLines") is not None
                else None,
            }
        )
