import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.address import Address
from yapily.models.hosted_vrp_account_identification import HostedVrpAccountIdentification


class HostedVrpPayerResponse(BaseModel):
    """
    __Conditional__. Details of the benefactor [person or business].  # noqa: E501
    """

    name: Annotated[StrictStr | None, Field(description="The account holder name of the Payer.")] = None
    account_identifications: Annotated[
        list[HostedVrpAccountIdentification],
        Field(
            alias="accountIdentifications",
            description="__Mandatory__. The account identifications that identify the `Payer` bank account.",
        ),
    ]
    address: Address | None = None
    __properties = ["name", "accountIdentifications", "address"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedVrpPayerResponse":
        """Create an instance of HostedVrpPayerResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict["address"] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedVrpPayerResponse":
        """Create an instance of HostedVrpPayerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedVrpPayerResponse.parse_obj(obj)

        return HostedVrpPayerResponse.parse_obj(
            {
                "name": obj.get("name"),
                "account_identifications": [
                    HostedVrpAccountIdentification.from_dict(_item) for _item in obj.get("accountIdentifications")
                ]
                if obj.get("accountIdentifications") is not None
                else None,
                "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            }
        )
