import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.amount import Amount


class TransactionChargeDetails(BaseModel):
    """
    Details the charges that will apply to the transaction.  # noqa: E501
    """

    charge_amount: Annotated[Amount | None, Field(alias="chargeAmount")] = None
    __properties = ["chargeAmount"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "TransactionChargeDetails":
        """Create an instance of TransactionChargeDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of charge_amount
        if self.charge_amount:
            _dict["chargeAmount"] = self.charge_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "TransactionChargeDetails":
        """Create an instance of TransactionChargeDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionChargeDetails.model_validate(obj)

        return TransactionChargeDetails.model_validate(
            {
                "charge_amount": Amount.from_dict(obj.get("chargeAmount"))
                if obj.get("chargeAmount") is not None
                else None
            }
        )
