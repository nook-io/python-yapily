import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class HostedAmountDetails(BaseModel):
    """
    The payment amount and currency  # noqa: E501
    """

    amount_to_pay: Annotated[
        Annotated[float, Field(ge=0.01, strict=True)] | Annotated[int, Field(ge=1, strict=True)],
        Field(alias="amountToPay", description="The payment amount"),
    ]
    currency: Annotated[StrictStr, Field(description="The [ISO 4217](https://www.xe.com/iso4217.php) currency code")]
    __properties = ["amountToPay", "currency"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedAmountDetails":
        """Create an instance of HostedAmountDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedAmountDetails":
        """Create an instance of HostedAmountDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedAmountDetails.model_validate(obj)

        return HostedAmountDetails.model_validate({"amount_to_pay": obj.get("amountToPay"), "currency": obj.get("currency")})
