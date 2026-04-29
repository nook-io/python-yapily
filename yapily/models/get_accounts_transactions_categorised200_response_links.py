import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class GetAccountsTransactionsCategorised200ResponseLinks(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseLinks
    """

    first: StrictStr | None = None
    prev: StrictStr | None = None
    var_self: Annotated[StrictStr | None, Field(alias="self")] = None
    next: StrictStr | None = None
    last: StrictStr | None = None
    __properties = ["first", "prev", "self", "next", "last"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetAccountsTransactionsCategorised200ResponseLinks":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "GetAccountsTransactionsCategorised200ResponseLinks":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseLinks.model_validate(obj)

        return GetAccountsTransactionsCategorised200ResponseLinks.model_validate(
            {
                "first": obj.get("first"),
                "prev": obj.get("prev"),
                "var_self": obj.get("self"),
                "next": obj.get("next"),
                "last": obj.get("last"),
            }
        )
