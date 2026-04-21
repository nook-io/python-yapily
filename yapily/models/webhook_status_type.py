import json

from aenum import Enum


class WebhookStatusType(str, Enum):
    """
    WebhookStatusType
    """

    """
    allowed enum values
    """
    ACTIVE = "active"
    PAUSED = "paused"

    @classmethod
    def from_json(cls, json_str: str) -> "WebhookStatusType":
        """Create an instance of WebhookStatusType from a JSON string"""
        return WebhookStatusType(json.loads(json_str))
