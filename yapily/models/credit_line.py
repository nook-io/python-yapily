import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.amount import Amount
from yapily.models.credit_line_type import CreditLineType


class CreditLine(BaseModel):
    """
    __Mandatory__. Details whether the account has access to a credit line from an `Institution`.  # noqa: E501
    """

    type: CreditLineType | None = None
    credit_line_amount: Annotated[Amount | None, Field(alias="creditLineAmount")] = None
    __properties = ["type", "creditLineAmount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CreditLine":
        """Create an instance of CreditLine from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of credit_line_amount
        if self.credit_line_amount:
            _dict["creditLineAmount"] = self.credit_line_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "CreditLine":
        """Create an instance of CreditLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreditLine.model_validate(obj)

        return CreditLine.model_validate(
            {
                "type": obj.get("type"),
                "credit_line_amount": Amount.from_dict(obj.get("creditLineAmount"))
                if obj.get("creditLineAmount") is not None
                else None,
            }
        )
