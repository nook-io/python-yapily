from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_categorisation import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_merchant import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_transaction_hash import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash,
)
from typing import Set
from typing_extensions import Self


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment(
    BaseModel
):
    categorisation: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation
    ] = None
    recurrence: Optional[StrictStr] = None
    transaction_hash: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash
    ] = Field(default=None, alias="transactionHash")
    merchant: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant
    ] = None
    payment_processor: Optional[StrictStr] = Field(
        default=None, alias="paymentProcessor"
    )
    __properties: ClassVar[List[str]] = [
        "categorisation",
        "recurrence",
        "transactionHash",
        "merchant",
        "paymentProcessor",
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
        if self.categorisation:
            _dict["categorisation"] = self.categorisation.to_dict()
        if self.transaction_hash:
            _dict["transactionHash"] = self.transaction_hash.to_dict()
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "categorisation": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation.from_dict(
                    obj["categorisation"]
                )
                if obj.get("categorisation") is not None
                else None,
                "recurrence": obj.get("recurrence"),
                "transactionHash": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash.from_dict(
                    obj["transactionHash"]
                )
                if obj.get("transactionHash") is not None
                else None,
                "merchant": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant.from_dict(
                    obj["merchant"]
                )
                if obj.get("merchant") is not None
                else None,
                "paymentProcessor": obj.get("paymentProcessor"),
            }
        )
        return _obj
