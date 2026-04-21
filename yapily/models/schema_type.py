import json

from aenum import Enum


class SchemaType(str, Enum):
    """
    SchemaType
    """

    """
    allowed enum values
    """
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

    @classmethod
    def from_json(cls, json_str: str) -> "SchemaType":
        """Create an instance of SchemaType from a JSON string"""
        return SchemaType(json.loads(json_str))
