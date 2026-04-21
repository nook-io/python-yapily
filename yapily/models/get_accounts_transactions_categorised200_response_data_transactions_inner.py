import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_balance import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_iso_bank_transaction_code import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_proprietary_bank_transaction_code import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_transaction_amount import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount,
)


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInner(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInner
    """

    id: StrictStr | None = None
    var_date: Annotated[StrictStr | None, Field(alias="date")] = None
    booking_date_time: Annotated[datetime | None, Field(alias="bookingDateTime")] = None
    value_date_time: Annotated[datetime | None, Field(alias="valueDateTime")] = None
    status: StrictStr | None = None
    amount: StrictInt | None = None
    currency: StrictStr | None = None
    transaction_amount: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount | None,
        Field(alias="transactionAmount"),
    ] = None
    reference: StrictStr | None = None
    description: StrictStr | None = None
    transaction_information: Annotated[list[StrictStr] | None, Field(alias="transactionInformation")] = None
    proprietary_bank_transaction_code: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode | None,
        Field(alias="proprietaryBankTransactionCode"),
    ] = None
    iso_bank_transaction_code: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode | None,
        Field(alias="isoBankTransactionCode"),
    ] = None
    balance: GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance | None = None
    enrichment: GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment | None = None
    hash: StrictStr | None = None
    __properties = [
        "id",
        "date",
        "bookingDateTime",
        "valueDateTime",
        "status",
        "amount",
        "currency",
        "transactionAmount",
        "reference",
        "description",
        "transactionInformation",
        "proprietaryBankTransactionCode",
        "isoBankTransactionCode",
        "balance",
        "enrichment",
        "hash",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInner":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction_amount
        if self.transaction_amount:
            _dict["transactionAmount"] = self.transaction_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proprietary_bank_transaction_code
        if self.proprietary_bank_transaction_code:
            _dict["proprietaryBankTransactionCode"] = self.proprietary_bank_transaction_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iso_bank_transaction_code
        if self.iso_bank_transaction_code:
            _dict["isoBankTransactionCode"] = self.iso_bank_transaction_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict["balance"] = self.balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enrichment
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInner":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.parse_obj(obj)

        return GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.parse_obj(
            {
                "id": obj.get("id"),
                "var_date": obj.get("date"),
                "booking_date_time": obj.get("bookingDateTime"),
                "value_date_time": obj.get("valueDateTime"),
                "status": obj.get("status"),
                "amount": obj.get("amount"),
                "currency": obj.get("currency"),
                "transaction_amount": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount.from_dict(
                    obj.get("transactionAmount")
                )
                if obj.get("transactionAmount") is not None
                else None,
                "reference": obj.get("reference"),
                "description": obj.get("description"),
                "transaction_information": obj.get("transactionInformation"),
                "proprietary_bank_transaction_code": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode.from_dict(
                    obj.get("proprietaryBankTransactionCode")
                )
                if obj.get("proprietaryBankTransactionCode") is not None
                else None,
                "iso_bank_transaction_code": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode.from_dict(
                    obj.get("isoBankTransactionCode")
                )
                if obj.get("isoBankTransactionCode") is not None
                else None,
                "balance": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance.from_dict(
                    obj.get("balance")
                )
                if obj.get("balance") is not None
                else None,
                "enrichment": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.from_dict(
                    obj.get("enrichment")
                )
                if obj.get("enrichment") is not None
                else None,
                "hash": obj.get("hash"),
            }
        )
