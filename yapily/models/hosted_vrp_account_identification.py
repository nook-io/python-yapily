import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class HostedVrpAccountIdentification(BaseModel):
    """
    HostedVrpAccountIdentification
    """

    type: Annotated[
        StrictStr,
        Field(
            description="Used to describe the format of the account.<br><br> Allowed values: <br>MASKED_ACCOUNT_NUMBER<br>SORT_CODE<br>ACCOUNT_NUMBER "
        ),
    ]
    identification: Annotated[
        StrictStr,
        Field(
            description="__Mandatory__. The value associated with the account identification type.<br><br> See [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#account-identifications-combinations) for more information on the format of the values."
        ),
    ]
    __properties = ["type", "identification"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedVrpAccountIdentification":
        """Create an instance of HostedVrpAccountIdentification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedVrpAccountIdentification":
        """Create an instance of HostedVrpAccountIdentification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedVrpAccountIdentification.parse_obj(obj)

        return HostedVrpAccountIdentification.parse_obj(
            {"type": obj.get("type"), "identification": obj.get("identification")}
        )
