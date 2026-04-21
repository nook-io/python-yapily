import json

from aenum import Enum


class EnvironmentType(str, Enum):
    """
    The environment type. <br><br>See [Institution Configuration](https://docs.yapily.com/pages/key-concepts/institutions/#configuration) for more information
    """

    """
    allowed enum values
    """
    SANDBOX = "SANDBOX"
    MOCK = "MOCK"
    LIVE = "LIVE"

    @classmethod
    def from_json(cls, json_str: str) -> "EnvironmentType":
        """Create an instance of EnvironmentType from a JSON string"""
        return EnvironmentType(json.loads(json_str))
