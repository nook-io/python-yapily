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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_categorisation import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_merchant import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant,
)
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_transaction_hash import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash,
)


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment(
    BaseModel
):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment
    """

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
    __properties = [
        "categorisation",
        "recurrence",
        "transactionHash",
        "merchant",
        "paymentProcessor",
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
    def from_json(
        cls, json_str: str
    ) -> GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment:
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of categorisation
        if self.categorisation:
            _dict["categorisation"] = self.categorisation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction_hash
        if self.transaction_hash:
            _dict["transactionHash"] = self.transaction_hash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment:
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.parse_obj(
                obj
            )

        _obj = GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.parse_obj(
            {
                "categorisation": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation.from_dict(
                    obj.get("categorisation")
                )
                if obj.get("categorisation") is not None
                else None,
                "recurrence": obj.get("recurrence"),
                "transaction_hash": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash.from_dict(
                    obj.get("transactionHash")
                )
                if obj.get("transactionHash") is not None
                else None,
                "merchant": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant.from_dict(
                    obj.get("merchant")
                )
                if obj.get("merchant") is not None
                else None,
                "payment_processor": obj.get("paymentProcessor"),
            }
        )
        return _obj
