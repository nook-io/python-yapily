import json

from aenum import Enum


class FrequencyEnum(str, Enum):
    """
    __Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [MONTHLY].
    """

    """
    allowed enum values
    """
    MONTHLY = "MONTHLY"

    @classmethod
    def from_json(cls, json_str: str) -> "FrequencyEnum":
        """Create an instance of FrequencyEnum from a JSON string"""
        return FrequencyEnum(json.loads(json_str))
