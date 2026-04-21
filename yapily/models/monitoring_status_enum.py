import json

from aenum import Enum


class MonitoringStatusEnum(str, Enum):
    """
    The latest operational status.
    """

    """
    allowed enum values
    """
    UP = "Up"
    DOWN = "Down"
    WARNING = "Warning"
    UNKNOWN = "Unknown"
    EXPIRED = "Expired"

    @classmethod
    def from_json(cls, json_str: str) -> "MonitoringStatusEnum":
        """Create an instance of MonitoringStatusEnum from a JSON string"""
        return MonitoringStatusEnum(json.loads(json_str))
