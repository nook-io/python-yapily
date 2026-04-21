import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class PaymentRisk(BaseModel):
    """
    Additional information about the payment that may be used for risk scoring  # noqa: E501
    """

    context_type: Annotated[
        StrictStr | None,
        Field(
            alias="contextType",
            description="__Optional__. The payment context code. Allowed values are [BILL_IN_ADVANCE, BILL_IN_ARREARS, ECOMMERCE_MERCHANT, FACE_TO_FACE_POS, TRANSFER_TO_SELF,TRANSFER_TO_THIRD_PARTY, PISP_PAYEE ].",
        ),
    ] = None
    __properties = ["contextType"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentRisk":
        """Create an instance of PaymentRisk from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "PaymentRisk":
        """Create an instance of PaymentRisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentRisk.parse_obj(obj)

        return PaymentRisk.parse_obj({"context_type": obj.get("contextType")})
