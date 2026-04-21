import json

from aenum import Enum


class AddressTypeEnum(str, Enum):
    """
    __Optional__. The type of address
    """

    """
    allowed enum values
    """
    BUSINESS = "BUSINESS"
    CORRESPONDENCE = "CORRESPONDENCE"
    DELIVERY_TO = "DELIVERY_TO"
    MAIL_TO = "MAIL_TO"
    PO_BOX = "PO_BOX"
    POSTAL = "POSTAL"
    RESIDENTIAL = "RESIDENTIAL"
    STATEMENT = "STATEMENT"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> "AddressTypeEnum":
        """Create an instance of AddressTypeEnum from a JSON string"""
        return AddressTypeEnum(json.loads(json_str))
