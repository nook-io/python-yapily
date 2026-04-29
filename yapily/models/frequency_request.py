import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt

from yapily.models.frequency_enum_extended import FrequencyEnumExtended


class FrequencyRequest(BaseModel):
    """
    __Mandatory__. Defines the intervals at which payment should be made.  # noqa: E501
    """

    type: Annotated[FrequencyEnumExtended, Field()]
    interval_week: Annotated[
        StrictInt | None,
        Field(
            alias="intervalWeek",
            description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        ),
    ] = None
    interval_month: Annotated[
        StrictInt | None,
        Field(
            alias="intervalMonth",
            description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        ),
    ] = None
    execution_day: Annotated[
        StrictInt | None,
        Field(
            alias="executionDay",
            description="__Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information",
        ),
    ] = None
    __properties = ["type", "intervalWeek", "intervalMonth", "executionDay"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FrequencyRequest":
        """Create an instance of FrequencyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "FrequencyRequest":
        """Create an instance of FrequencyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrequencyRequest.model_validate(obj)

        return FrequencyRequest.model_validate(
            {
                "type": obj.get("type"),
                "interval_week": obj.get("intervalWeek"),
                "interval_month": obj.get("intervalMonth"),
                "execution_day": obj.get("executionDay"),
            }
        )
