import json

from aenum import Enum


class AddressTypeEnumResponse(str, Enum):
    """
    The type of address
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
    def from_json(cls, json_str: str) -> "AddressTypeEnumResponse":
        """Create an instance of AddressTypeEnumResponse from a JSON string"""
        return AddressTypeEnumResponse(json.loads(json_str))
