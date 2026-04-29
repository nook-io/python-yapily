import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.account_identification import AccountIdentification


class PayeeDetails(BaseModel):
    """
    __Mandatory__. Details of the beneficiary [person or business].  # noqa: E501
    """

    name: Annotated[StrictStr, Field(description="__Mandatory__. The account holder name of the beneficiary.")]
    account_identifications: Annotated[
        list[AccountIdentification],
        Field(
            alias="accountIdentifications",
            description="__Mandatory__. The account identifications that identify the `Payee` bank account.",
        ),
    ]
    country: Annotated[
        StrictStr,
        Field(
            description="__Conditional__. The 2-letter ISO 3166 country code for the address. <br><br>An `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to make a payment"
        ),
    ]
    __properties = ["name", "accountIdentifications", "country"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PayeeDetails":
        """Create an instance of PayeeDetails from a JSON string"""
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
    def from_dict(cls, obj: dict) -> "PayeeDetails":
        """Create an instance of PayeeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayeeDetails.model_validate(obj)

        return PayeeDetails.model_validate(
            {
                "name": obj.get("name"),
                "account_identifications": [
                    AccountIdentification.from_dict(_item) for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
                "country": obj.get("country"),
            }
        )
