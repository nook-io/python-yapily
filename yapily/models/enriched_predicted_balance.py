import json
import pprint
from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt


class EnrichedPredictedBalance(BaseModel):
    """
    A list of Predicted Account Balances for future date range.  # noqa: E501
    """

    var_date: Annotated[
        date | None, Field(alias="date", description="The date for which Balance amount is predicted.")
    ] = None
    median_balance: Annotated[
        StrictFloat | StrictInt | None,
        Field(alias="medianBalance", description="The median Balance amount for a future date."),
    ] = None
    var_90percentile_balance: Annotated[
        StrictFloat | StrictInt | None,
        Field(alias="90percentileBalance", description="The 90th percentile Balance amount for a future date."),
    ] = None
    var_10percentile_balance: Annotated[
        StrictFloat | StrictInt | None,
        Field(alias="10percentileBalance", description="The 10th percentile Balance amount for a future date."),
    ] = None
    __properties = ["date", "medianBalance", "90percentileBalance", "10percentileBalance"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EnrichedPredictedBalance":
        """Create an instance of EnrichedPredictedBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "EnrichedPredictedBalance":
        """Create an instance of EnrichedPredictedBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedPredictedBalance.model_validate(obj)

        return EnrichedPredictedBalance.model_validate(
            {
                "var_date": obj.get("date"),
                "median_balance": obj.get("medianBalance"),
                "var_90percentile_balance": obj.get("90percentileBalance"),
                "var_10percentile_balance": obj.get("10percentileBalance"),
            }
        )
