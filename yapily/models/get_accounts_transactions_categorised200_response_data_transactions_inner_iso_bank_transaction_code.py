from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_iso_bank_transaction_code_domain_code import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode,
)
from typing import Set
from typing_extensions import Self


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode(
    BaseModel
):
    domain_code: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode
    ] = Field(default=None, alias="domainCode")
    family_code: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode
    ] = Field(default=None, alias="familyCode")
    sub_family_code: Optional[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode
    ] = Field(default=None, alias="subFamilyCode")
    __properties: ClassVar[List[str]] = ["domainCode", "familyCode", "subFamilyCode"]
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
        if self.domain_code:
            _dict["domainCode"] = self.domain_code.to_dict()
        if self.family_code:
            _dict["familyCode"] = self.family_code.to_dict()
        if self.sub_family_code:
            _dict["subFamilyCode"] = self.sub_family_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "domainCode": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj["domainCode"]
                )
                if obj.get("domainCode") is not None
                else None,
                "familyCode": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj["familyCode"]
                )
                if obj.get("familyCode") is not None
                else None,
                "subFamilyCode": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj["subFamilyCode"]
                )
                if obj.get("subFamilyCode") is not None
                else None,
            }
        )
        return _obj
