import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt

from yapily.models.frequency_enum_extended import FrequencyEnumExtended


class FrequencyResponse(BaseModel):
    """
    __Mandatory__. Defines the intervals at which payment should be made.  # noqa: E501
    """

    frequency_type: Annotated[FrequencyEnumExtended | None, Field(alias="frequencyType")] = None
    interval_week: Annotated[
        StrictInt | None,
        Field(
            alias="intervalWeek",
            description="The weekly intervals at which a payment will be made. e.g. 1 = Every months, 2 = Every 2 months.",
        ),
    ] = None
    interval_month: Annotated[
        StrictInt | None,
        Field(
            alias="intervalMonth",
            description="The monthly intervals at which a payment will be made. e.g. 1 = Every month, 2 = Every 2 months",
        ),
    ] = None
    execution_day: Annotated[
        StrictInt | None,
        Field(
            alias="executionDay",
            description="The day on which a payment will be made, according to the weekly or monthly interval.",
        ),
    ] = None
    __properties = ["frequencyType", "intervalWeek", "intervalMonth", "executionDay"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FrequencyResponse":
        """Create an instance of FrequencyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "FrequencyResponse":
        """Create an instance of FrequencyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrequencyResponse.parse_obj(obj)

        return FrequencyResponse.parse_obj(
            {
                "frequency_type": obj.get("frequencyType"),
                "interval_week": obj.get("intervalWeek"),
                "interval_month": obj.get("intervalMonth"),
                "execution_day": obj.get("executionDay"),
            }
        )
