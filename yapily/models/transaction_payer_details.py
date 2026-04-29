import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.transaction_payee_details_account_identifications_inner import (
    TransactionPayeeDetailsAccountIdentificationsInner,
)


class TransactionPayerDetails(BaseModel):
    """
    Details of the benefactor [person or business].  # noqa: E501
    """

    name: Annotated[StrictStr | None, Field(description="The account holder name of the Payer.")] = None
    account_identifications: Annotated[
        list[TransactionPayeeDetailsAccountIdentificationsInner] | None,
        Field(
            alias="accountIdentifications",
            description="The account identifications that identify the Payer's bank account.",
        ),
    ] = None
    __properties = ["name", "accountIdentifications"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "TransactionPayerDetails":
        """Create an instance of TransactionPayerDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifications (list)
        _items = []
        if self.account_identifications:
            for _item in self.account_identifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountIdentifications"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "TransactionPayerDetails":
        """Create an instance of TransactionPayerDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionPayerDetails.model_validate(obj)

        return TransactionPayerDetails.model_validate(
            {
                "name": obj.get("name"),
                "account_identifications": [
                    TransactionPayeeDetailsAccountIdentificationsInner.from_dict(_item)
                    for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
            }
        )
