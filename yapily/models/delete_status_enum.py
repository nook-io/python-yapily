import json

from aenum import Enum


class DeleteStatusEnum(str, Enum):
    """
    Indicates the outcome of the delete request.
    """

    """
    allowed enum values
    """
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

    @classmethod
    def from_json(cls, json_str: str) -> "DeleteStatusEnum":
        """Create an instance of DeleteStatusEnum from a JSON string"""
        return DeleteStatusEnum(json.loads(json_str))
