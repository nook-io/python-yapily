import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr


class TransactionSchedule(BaseModel):
    """
    The frequency at which transactions occurred.  # noqa: E501
    """

    frequency: Annotated[
        StrictStr | None,
        Field(
            description="How often the transaction happens.  Can be 'Monthly', 'Twice monthly', 'Every two weeks', 'Every four weeks', 'Daily', 'Weekly', 'Every weekday', 'Twice daily', 'Twice every weekday'"
        ),
    ] = None
    detailed_frequency: Annotated[
        StrictStr | None,
        Field(
            alias="detailedFrequency",
            description="When in the cycle the transaction occurs.  Can be 'Daily', 'Twice daily', 'Twice every weekday', 'Every weekday', 'Weekly on day n', 'Every two weeks on day n', 'Monthly on working day before day n of month', 'Monthly on last working day of month', 'Twice a month on 15th and last working day of month', 'Every four weeks on day n'",
        ),
    ] = None
    detailed_frequency_parameter: Annotated[
        StrictFloat | StrictInt | None,
        Field(
            alias="detailedFrequencyParameter",
            description="The n in detailedFrequency where there is one - for week-based frequencies, an integer from 0 to 6 where 0 is Monday or for month-based frequencies, an integer from 0 to 27 where 0 is the first day of the month",
        ),
    ] = None
    __properties = ["frequency", "detailedFrequency", "detailedFrequencyParameter"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "TransactionSchedule":
        """Create an instance of TransactionSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "TransactionSchedule":
        """Create an instance of TransactionSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionSchedule.model_validate(obj)

        return TransactionSchedule.model_validate(
            {
                "frequency": obj.get("frequency"),
                "detailed_frequency": obj.get("detailedFrequency"),
                "detailed_frequency_parameter": obj.get("detailedFrequencyParameter"),
            }
        )
