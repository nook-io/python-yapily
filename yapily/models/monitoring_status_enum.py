import json
from aenum import Enum


class MonitoringStatusEnum(str, Enum):
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
        return MonitoringStatusEnum(json.loads(json_str))
