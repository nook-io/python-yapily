import json

from aenum import Enum


class Type(str, Enum):
    """
    The `SCA` method type available for the user
    """

    """
    allowed enum values
    """
    SMS_OTP = "SMS_OTP"
    CHIP_OTP = "CHIP_OTP"
    PHOTO_OTP = "PHOTO_OTP"
    PUSH_OTP = "PUSH_OTP"

    @classmethod
    def from_json(cls, json_str: str) -> "Type":
        """Create an instance of Type from a JSON string"""
        return Type(json.loads(json_str))
