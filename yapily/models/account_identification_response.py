import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.account_identification_type_response import AccountIdentificationTypeResponse


class AccountIdentificationResponse(BaseModel):
    """
    AccountIdentificationResponse
    """

    type: AccountIdentificationTypeResponse | None = None
    identification: Annotated[
        StrictStr | None,
        Field(
            description="The value associated with the account identification type.<br><br> See [Account Identification Combinations](https://docs.yapily.com/pages/payments/payments-resources/intro-to-payment-execution/#account-identifications-combinations) for more information on the format of the values."
        ),
    ] = None
    __properties = ["type", "identification"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AccountIdentificationResponse":
        """Create an instance of AccountIdentificationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "AccountIdentificationResponse":
        """Create an instance of AccountIdentificationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountIdentificationResponse.parse_obj(obj)

        return AccountIdentificationResponse.parse_obj(
            {"type": obj.get("type"), "identification": obj.get("identification")}
        )
