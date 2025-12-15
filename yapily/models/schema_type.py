from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SchemaType(str, Enum):
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
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
