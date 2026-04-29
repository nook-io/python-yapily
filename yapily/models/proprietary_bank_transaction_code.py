import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ProprietaryBankTransactionCode(BaseModel):
    """
    Transaction code that is proprietary to the `Institution`.  # noqa: E501
    """

    code: Annotated[
        StrictStr | None,
        Field(description="__Mandatory__. Properietary code used to identify the underlying transaction."),
    ] = None
    issuer: Annotated[StrictStr | None, Field(description="__Mandatory__. Issuer of the properitary code.")] = None
    __properties = ["code", "issuer"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ProprietaryBankTransactionCode":
        """Create an instance of ProprietaryBankTransactionCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ProprietaryBankTransactionCode":
        """Create an instance of ProprietaryBankTransactionCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProprietaryBankTransactionCode.model_validate(obj)

        return ProprietaryBankTransactionCode.model_validate({"code": obj.get("code"), "issuer": obj.get("issuer")})
