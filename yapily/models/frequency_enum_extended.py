from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FrequencyEnumExtended(str, Enum):
    """
    allowed enum values
    """

    DAILY = "DAILY"
    EVERY_WORKING_DAY = "EVERY_WORKING_DAY"
    CALENDAR_DAY = "CALENDAR_DAY"
    WEEKLY = "WEEKLY"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    MONTHLY = "MONTHLY"
    EVERY_TWO_MONTHS = "EVERY_TWO_MONTHS"
    QUARTERLY = "QUARTERLY"
    SEMIANNUAL = "SEMIANNUAL"
    ANNUAL = "ANNUAL"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
