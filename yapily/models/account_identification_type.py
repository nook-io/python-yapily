from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AccountIdentificationType(str, Enum):
    """
    allowed enum values
    """

    SORT_CODE = "SORT_CODE"
    ACCOUNT_NUMBER = "ACCOUNT_NUMBER"
    IBAN = "IBAN"
    BBAN = "BBAN"
    BIC = "BIC"
    PAN = "PAN"
    MASKED_PAN = "MASKED_PAN"
    MSISDN = "MSISDN"
    BSB = "BSB"
    NCC = "NCC"
    ABA = "ABA"
    ABA_WIRE = "ABA_WIRE"
    ABA_ACH = "ABA_ACH"
    EMAIL = "EMAIL"
    ROLL_NUMBER = "ROLL_NUMBER"
    BLZ = "BLZ"
    IFS = "IFS"
    CLABE = "CLABE"
    CTN = "CTN"
    BRANCH_CODE = "BRANCH_CODE"
    VIRTUAL_ACCOUNT_ID = "VIRTUAL_ACCOUNT_ID"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
