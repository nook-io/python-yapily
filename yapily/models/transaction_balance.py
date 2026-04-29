import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.account_balance_type import AccountBalanceType
from yapily.models.amount import Amount


class TransactionBalance(BaseModel):
    """
    TransactionBalance
    """

    type: AccountBalanceType | None = None
    balance_amount: Annotated[Amount | None, Field(alias="balanceAmount")] = None
    __properties = ["type", "balanceAmount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "TransactionBalance":
        """Create an instance of TransactionBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of balance_amount
        if self.balance_amount:
            _dict["balanceAmount"] = self.balance_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "TransactionBalance":
        """Create an instance of TransactionBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionBalance.model_validate(obj)

        return TransactionBalance.model_validate(
            {
                "type": obj.get("type"),
                "balance_amount": Amount.from_dict(obj.get("balanceAmount"))
                if obj.get("balanceAmount") is not None
                else None,
            }
        )
