from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Type(str, Enum):
    """
    allowed enum values
    """

    SMS_OTP = "SMS_OTP"
    CHIP_OTP = "CHIP_OTP"
    PHOTO_OTP = "PHOTO_OTP"
    PUSH_OTP = "PUSH_OTP"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
