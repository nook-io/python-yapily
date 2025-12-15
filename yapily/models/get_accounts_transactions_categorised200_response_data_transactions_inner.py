from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
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
from typing import Set
from typing_extensions import Self


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInner(BaseModel):
    id: Optional[StrictStr] = None
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    booking_date_time: Optional[datetime] = Field(default=None, alias="bookingDateTime")
    value_date_time: Optional[datetime] = Field(default=None, alias="valueDateTime")
    status: Optional[StrictStr] = None
    amount: Optional[StrictInt] = None
    currency: Optional[StrictStr] = None
    transaction_amount: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount
    ] = Field(default=None, alias="transactionAmount")
    reference: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    transaction_information: Optional[List[StrictStr]] = Field(
        default=None, alias="transactionInformation"
    )
    proprietary_bank_transaction_code: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode
    ] = Field(default=None, alias="proprietaryBankTransactionCode")
    iso_bank_transaction_code: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode
    ] = Field(default=None, alias="isoBankTransactionCode")
    balance: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance
    ] = None
    enrichment: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment
    ] = None
    hash: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
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
        if self.transaction_amount:
            _dict["transactionAmount"] = self.transaction_amount.to_dict()
        if self.proprietary_bank_transaction_code:
            _dict["proprietaryBankTransactionCode"] = (
                self.proprietary_bank_transaction_code.to_dict()
            )
        if self.iso_bank_transaction_code:
            _dict["isoBankTransactionCode"] = self.iso_bank_transaction_code.to_dict()
        if self.balance:
            _dict["balance"] = self.balance.to_dict()
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "date": obj.get("date"),
                "bookingDateTime": obj.get("bookingDateTime"),
                "valueDateTime": obj.get("valueDateTime"),
                "status": obj.get("status"),
                "amount": obj.get("amount"),
                "currency": obj.get("currency"),
                "transactionAmount": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount.from_dict(
                    obj["transactionAmount"]
                )
                if obj.get("transactionAmount") is not None
                else None,
                "reference": obj.get("reference"),
                "description": obj.get("description"),
                "transactionInformation": obj.get("transactionInformation"),
                "proprietaryBankTransactionCode": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode.from_dict(
                    obj["proprietaryBankTransactionCode"]
                )
                if obj.get("proprietaryBankTransactionCode") is not None
                else None,
                "isoBankTransactionCode": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode.from_dict(
                    obj["isoBankTransactionCode"]
                )
                if obj.get("isoBankTransactionCode") is not None
                else None,
                "balance": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance.from_dict(
                    obj["balance"]
                )
                if obj.get("balance") is not None
                else None,
                "enrichment": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.from_dict(
                    obj["enrichment"]
                )
                if obj.get("enrichment") is not None
                else None,
                "hash": obj.get("hash"),
            }
        )
        return _obj
