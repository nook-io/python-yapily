# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self


class TransactionSchedule(BaseModel):
    """
    The frequency at which transactions occurred.
    """  # noqa: E501

    frequency: Optional[StrictStr] = Field(
        default=None,
        description="How often the transaction happens.  Can be 'Monthly', 'Twice monthly', 'Every two weeks', 'Every four weeks', 'Daily', 'Weekly', 'Every weekday', 'Twice daily', 'Twice every weekday'",
    )
    detailed_frequency: Optional[StrictStr] = Field(
        default=None,
        description="When in the cycle the transaction occurs.  Can be 'Daily', 'Twice daily', 'Twice every weekday', 'Every weekday', 'Weekly on day n', 'Every two weeks on day n', 'Monthly on working day before day n of month', 'Monthly on last working day of month', 'Twice a month on 15th and last working day of month', 'Every four weeks on day n'",
        alias="detailedFrequency",
    )
    detailed_frequency_parameter: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The n in detailedFrequency where there is one - for week-based frequencies, an integer from 0 to 6 where 0 is Monday or for month-based frequencies, an integer from 0 to 27 where 0 is the first day of the month",
        alias="detailedFrequencyParameter",
    )
    __properties: ClassVar[List[str]] = [
        "frequency",
        "detailedFrequency",
        "detailedFrequencyParameter",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "frequency": obj.get("frequency"),
                "detailedFrequency": obj.get("detailedFrequency"),
                "detailedFrequencyParameter": obj.get("detailedFrequencyParameter"),
            }
        )
        return _obj
