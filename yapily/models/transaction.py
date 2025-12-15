from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from yapily.models.address_details import AddressDetails
from yapily.models.amount import Amount
from yapily.models.currency_exchange import CurrencyExchange
from yapily.models.enrichment import Enrichment
from yapily.models.iso_bank_transaction_code import IsoBankTransactionCode
from yapily.models.merchant import Merchant
from yapily.models.proprietary_bank_transaction_code import (
    ProprietaryBankTransactionCode,
)
from yapily.models.statement_reference import StatementReference
from yapily.models.transaction_balance import TransactionBalance
from yapily.models.transaction_charge_details import TransactionChargeDetails
from yapily.models.transaction_payee_details import TransactionPayeeDetails
from yapily.models.transaction_payer_details import TransactionPayerDetails
from yapily.models.transaction_status_enum import TransactionStatusEnum
from typing import Set
from typing_extensions import Self


class Transaction(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the transaction."
    )
    var_date: Optional[datetime] = Field(default=None, alias="date")
    booking_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time in UTC format of when a transaction was booked.",
        alias="bookingDateTime",
    )
    value_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time in UTC format when the funds either cease to be available (for debit transactions) or become available (for credit transactions) to the account owner.",
        alias="valueDateTime",
    )
    status: Optional[TransactionStatusEnum] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="The transaction amount."
    )
    currency: Optional[StrictStr] = Field(
        default=None,
        description="Currency the transaction amount is denoted in. Specified as a 3-letter ISO 4217 code.",
    )
    transaction_amount: Optional[Amount] = Field(
        default=None, alias="transactionAmount"
    )
    gross_amount: Optional[Amount] = Field(default=None, alias="grossAmount")
    currency_exchange: Optional[CurrencyExchange] = Field(
        default=None, alias="currencyExchange"
    )
    charge_details: Optional[TransactionChargeDetails] = Field(
        default=None, alias="chargeDetails"
    )
    reference: Optional[StrictStr] = None
    statement_references: Optional[List[StatementReference]] = Field(
        default=None, alias="statementReferences"
    )
    description: Optional[StrictStr] = None
    transaction_information: Optional[List[StrictStr]] = Field(
        default=None,
        description="Further details on the transaction. This is narrative data, caught as unstructured text.",
        alias="transactionInformation",
    )
    address_details: Optional[AddressDetails] = Field(
        default=None, alias="addressDetails"
    )
    iso_bank_transaction_code: Optional[IsoBankTransactionCode] = Field(
        default=None, alias="isoBankTransactionCode"
    )
    proprietary_bank_transaction_code: Optional[ProprietaryBankTransactionCode] = Field(
        default=None, alias="proprietaryBankTransactionCode"
    )
    balance: Optional[TransactionBalance] = None
    payee_details: Optional[TransactionPayeeDetails] = Field(
        default=None, alias="payeeDetails"
    )
    payer_details: Optional[TransactionPayerDetails] = Field(
        default=None, alias="payerDetails"
    )
    merchant: Optional[Merchant] = None
    enrichment: Optional[Enrichment] = None
    supplementary_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional information that cannot be captured in a structured field or block.",
        alias="supplementaryData",
    )
    transaction_mutability: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. Specifies the Mutability of the Transaction record.<ul><li>A transaction with a `Status` of `Pending` is mutable.</li><li>A transaction with a `Status` of `Booked` where the `TransactionMutability` flag is not specified is not guaranteed to be immutable (although in most instances it will be).</li><li>A transaction with a `Status` of `Booked` with the `TransactionMutability` flag set to `Immutable` is immutable.</li><li>A transaction with a `Status` of `Booked` with the `TransactionMutability` flag set to `Mutable` is mutable.</li></ul>",
        alias="transactionMutability",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "date",
        "bookingDateTime",
        "valueDateTime",
        "status",
        "amount",
        "currency",
        "transactionAmount",
        "grossAmount",
        "currencyExchange",
        "chargeDetails",
        "reference",
        "statementReferences",
        "description",
        "transactionInformation",
        "addressDetails",
        "isoBankTransactionCode",
        "proprietaryBankTransactionCode",
        "balance",
        "payeeDetails",
        "payerDetails",
        "merchant",
        "enrichment",
        "supplementaryData",
        "transactionMutability",
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
        if self.gross_amount:
            _dict["grossAmount"] = self.gross_amount.to_dict()
        if self.currency_exchange:
            _dict["currencyExchange"] = self.currency_exchange.to_dict()
        if self.charge_details:
            _dict["chargeDetails"] = self.charge_details.to_dict()
        _items = []
        if self.statement_references:
            for _item_statement_references in self.statement_references:
                if _item_statement_references:
                    _items.append(_item_statement_references.to_dict())
            _dict["statementReferences"] = _items
        if self.address_details:
            _dict["addressDetails"] = self.address_details.to_dict()
        if self.iso_bank_transaction_code:
            _dict["isoBankTransactionCode"] = self.iso_bank_transaction_code.to_dict()
        if self.proprietary_bank_transaction_code:
            _dict["proprietaryBankTransactionCode"] = (
                self.proprietary_bank_transaction_code.to_dict()
            )
        if self.balance:
            _dict["balance"] = self.balance.to_dict()
        if self.payee_details:
            _dict["payeeDetails"] = self.payee_details.to_dict()
        if self.payer_details:
            _dict["payerDetails"] = self.payer_details.to_dict()
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
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
                "transactionAmount": Amount.from_dict(obj["transactionAmount"])
                if obj.get("transactionAmount") is not None
                else None,
                "grossAmount": Amount.from_dict(obj["grossAmount"])
                if obj.get("grossAmount") is not None
                else None,
                "currencyExchange": CurrencyExchange.from_dict(obj["currencyExchange"])
                if obj.get("currencyExchange") is not None
                else None,
                "chargeDetails": TransactionChargeDetails.from_dict(
                    obj["chargeDetails"]
                )
                if obj.get("chargeDetails") is not None
                else None,
                "reference": obj.get("reference"),
                "statementReferences": [
                    StatementReference.from_dict(_item)
                    for _item in obj["statementReferences"]
                ]
                if obj.get("statementReferences") is not None
                else None,
                "description": obj.get("description"),
                "transactionInformation": obj.get("transactionInformation"),
                "addressDetails": AddressDetails.from_dict(obj["addressDetails"])
                if obj.get("addressDetails") is not None
                else None,
                "isoBankTransactionCode": IsoBankTransactionCode.from_dict(
                    obj["isoBankTransactionCode"]
                )
                if obj.get("isoBankTransactionCode") is not None
                else None,
                "proprietaryBankTransactionCode": ProprietaryBankTransactionCode.from_dict(
                    obj["proprietaryBankTransactionCode"]
                )
                if obj.get("proprietaryBankTransactionCode") is not None
                else None,
                "balance": TransactionBalance.from_dict(obj["balance"])
                if obj.get("balance") is not None
                else None,
                "payeeDetails": TransactionPayeeDetails.from_dict(obj["payeeDetails"])
                if obj.get("payeeDetails") is not None
                else None,
                "payerDetails": TransactionPayerDetails.from_dict(obj["payerDetails"])
                if obj.get("payerDetails") is not None
                else None,
                "merchant": Merchant.from_dict(obj["merchant"])
                if obj.get("merchant") is not None
                else None,
                "enrichment": Enrichment.from_dict(obj["enrichment"])
                if obj.get("enrichment") is not None
                else None,
                "supplementaryData": obj.get("supplementaryData"),
                "transactionMutability": obj.get("transactionMutability"),
            }
        )
        return _obj
