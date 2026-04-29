import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_iso_bank_transaction_code_domain_code import (
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode,
)


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode
    """

    domain_code: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode | None,
        Field(alias="domainCode"),
    ] = None
    family_code: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode | None,
        Field(alias="familyCode"),
    ] = None
    sub_family_code: Annotated[
        GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode | None,
        Field(alias="subFamilyCode"),
    ] = None
    __properties = ["domainCode", "familyCode", "subFamilyCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of domain_code
        if self.domain_code:
            _dict["domainCode"] = self.domain_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of family_code
        if self.family_code:
            _dict["familyCode"] = self.family_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_family_code
        if self.sub_family_code:
            _dict["subFamilyCode"] = self.sub_family_code.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode.model_validate(
                obj
            )

        return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode.model_validate(
            {
                "domain_code": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj.get("domainCode")
                )
                if obj.get("domainCode") is not None
                else None,
                "family_code": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj.get("familyCode")
                )
                if obj.get("familyCode") is not None
                else None,
                "sub_family_code": GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.from_dict(
                    obj.get("subFamilyCode")
                )
                if obj.get("subFamilyCode") is not None
                else None,
            }
        )
