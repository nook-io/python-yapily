import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class HostedPaymentIsoStatus(BaseModel):
    """
    The ISO status of the payment.  # noqa: E501
    """

    code: Annotated[
        StrictStr | None,
        Field(
            description="The ISO 20022 `PaymentStatusCode`. One of : <br> ACSC <br> ACCC <br> ACCP  <br> ACSP <br> ACTC <br> ACWC <br> ACWP <br> ACFC <br> RCVD <br> PART <br> PATC <br> PDNG <br> RJCT <br> CANC"
        ),
    ] = None
    name: Annotated[StrictStr | None, Field(description="The full name of the ISO 20022 `PaymentStatusCode`.")] = None
    __properties = ["code", "name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "HostedPaymentIsoStatus":
        """Create an instance of HostedPaymentIsoStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "HostedPaymentIsoStatus":
        """Create an instance of HostedPaymentIsoStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostedPaymentIsoStatus.model_validate(obj)

        return HostedPaymentIsoStatus.model_validate({"code": obj.get("code"), "name": obj.get("name")})
