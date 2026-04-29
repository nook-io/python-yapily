import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.payment_iso_status_code_enum import PaymentIsoStatusCodeEnum


class PaymentIsoStatus(BaseModel):
    """
    The payment status code, as denoted by a 3-letter ISO 20022 code.  # noqa: E501
    """

    code: PaymentIsoStatusCodeEnum | None = None
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
    def from_json(cls, json_str: str) -> "PaymentIsoStatus":
        """Create an instance of PaymentIsoStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "PaymentIsoStatus":
        """Create an instance of PaymentIsoStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentIsoStatus.model_validate(obj)

        return PaymentIsoStatus.model_validate({"code": obj.get("code"), "name": obj.get("name")})
