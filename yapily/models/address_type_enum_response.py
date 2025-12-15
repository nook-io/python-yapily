from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddressTypeEnumResponse(str, Enum):
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
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
