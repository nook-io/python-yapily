import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.account_identification import AccountIdentification


class RefundAccount(BaseModel):
    """
    The account to which funds should be returned if the payment is to be later refunded.  # noqa: E501
    """

    name: StrictStr | None = None
    account_identifications: Annotated[list[AccountIdentification] | None, Field(alias="accountIdentifications")] = None
    __properties = ["name", "accountIdentifications"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RefundAccount":
        """Create an instance of RefundAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in account_identifications (list)
        _items = []
        if self.account_identifications:
            for _item in self.account_identifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["accountIdentifications"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RefundAccount":
        """Create an instance of RefundAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RefundAccount.parse_obj(obj)

        return RefundAccount.parse_obj(
            {
                "name": obj.get("name"),
                "account_identifications": [
                    AccountIdentification.from_dict(_item) for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
            }
        )
