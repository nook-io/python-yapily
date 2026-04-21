import json

from aenum import Enum


class ChargeBearerType(str, Enum):
    """
    __Optional__. Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Valid values are:<ul><li>`DEBT` - All transaction charges are to be borne by the debtor.</li><li>`CRED` - All transaction charges are to be borne by the creditor.</li><li>`SHAR` - In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor</li><li>`SLEV` - Charges are to be applied following the rules agreed in the service level and/or scheme.</li></ul>
    """

    """
    allowed enum values
    """
    DEBT = "DEBT"
    CRED = "CRED"
    SHAR = "SHAR"
    SLEV = "SLEV"

    @classmethod
    def from_json(cls, json_str: str) -> "ChargeBearerType":
        """Create an instance of ChargeBearerType from a JSON string"""
        return ChargeBearerType(json.loads(json_str))
