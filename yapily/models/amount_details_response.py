import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr


class AmountDetailsResponse(BaseModel):
    """
    Monetary Amount.  # noqa: E501
    """

    amount: Annotated[StrictFloat | StrictInt | None, Field(description="The monetary value")] = None
    currency: Annotated[
        StrictStr | None, Field(description="The [ISO 4217](https://www.xe.com/iso4217.php) currency code")
    ] = None
    __properties = ["amount", "currency"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AmountDetailsResponse":
        """Create an instance of AmountDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "AmountDetailsResponse":
        """Create an instance of AmountDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AmountDetailsResponse.model_validate(obj)

        return AmountDetailsResponse.model_validate({"amount": obj.get("amount"), "currency": obj.get("currency")})
