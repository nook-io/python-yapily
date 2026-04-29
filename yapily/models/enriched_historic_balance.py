import json
import pprint
from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt


class EnrichedHistoricBalance(BaseModel):
    """
    A list of Aggregated Account Balances for historic date range.  # noqa: E501
    """

    var_date: Annotated[
        date | None,
        Field(
            alias="date", description="The date for which Aggregated Balance amount across Bank accounts is calculated."
        ),
    ] = None
    balance: Annotated[
        StrictFloat | StrictInt | None, Field(description="The Aggregated Balance amount for a specific date.")
    ] = None
    __properties = ["date", "balance"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EnrichedHistoricBalance":
        """Create an instance of EnrichedHistoricBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "EnrichedHistoricBalance":
        """Create an instance of EnrichedHistoricBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedHistoricBalance.model_validate(obj)

        return EnrichedHistoricBalance.model_validate({"var_date": obj.get("date"), "balance": obj.get("balance")})
