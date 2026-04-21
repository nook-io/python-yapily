import json

from aenum import Enum


class FrequencyEnumExtended(str, Enum):
    """
    __Mandatory__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information
    """

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
    def from_json(cls, json_str: str) -> "FrequencyEnumExtended":
        """Create an instance of FrequencyEnumExtended from a JSON string"""
        return FrequencyEnumExtended(json.loads(json_str))
