import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode
    """

    code: StrictStr | None = None
    name: StrictStr | None = None
    __properties = ["code", "name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.parse_obj(
                obj
            )

        return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCodeDomainCode.parse_obj(
            {"code": obj.get("code"), "name": obj.get("name")}
        )
