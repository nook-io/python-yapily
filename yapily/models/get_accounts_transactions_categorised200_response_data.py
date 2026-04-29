import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInner,
)


class GetAccountsTransactionsCategorised200ResponseData(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseData
    """

    transactions: (
        Annotated[list[GetAccountsTransactionsCategorised200ResponseDataTransactionsInner], Field()] | None
    ) = None
    __properties = ["transactions"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetAccountsTransactionsCategorised200ResponseData":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict["transactions"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetAccountsTransactionsCategorised200ResponseData":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseData.model_validate(obj)

        return GetAccountsTransactionsCategorised200ResponseData.model_validate(
            {
                "transactions": [
                    GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.from_dict(_item)
                    for _item in obj.get("transactions")
                ]
                if obj.get("transactions") is not None
                else None
            }
        )
