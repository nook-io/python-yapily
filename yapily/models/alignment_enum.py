import json

from aenum import Enum


class AlignmentEnum(str, Enum):
    """
    __Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question.
    """

    """
    allowed enum values
    """
    CONSENT = "CONSENT"
    CALENDAR = "CALENDAR"

    @classmethod
    def from_json(cls, json_str: str) -> "AlignmentEnum":
        """Create an instance of AlignmentEnum from a JSON string"""
        return AlignmentEnum(json.loads(json_str))
