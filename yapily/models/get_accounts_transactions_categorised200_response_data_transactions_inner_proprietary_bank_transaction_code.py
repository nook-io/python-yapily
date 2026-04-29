import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode
    """

    code: StrictStr | None = None
    issuer: StrictStr | None = None
    __properties = ["code", "issuer"]
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
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode.model_validate(
                obj
            )

        return (
            GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode.model_validate(
                {"code": obj.get("code"), "issuer": obj.get("issuer")}
            )
        )
