import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from yapily.models.beneficiary_payee import BeneficiaryPayee


class Beneficiary(BaseModel):
    """
    Account information belonging to the target beneficiary (person/ business).  # noqa: E501
    """

    id: Annotated[StrictStr | None, Field(description="Unique identifier of the `beneficiary`.")] = None
    reference: Annotated[
        StrictStr | None,
        Field(
            description="A creditor reference that is requested to be used for all payment instructions to this beneficiary."
        ),
    ] = None
    payee: BeneficiaryPayee | None = None
    trusted: Annotated[
        StrictBool | None,
        Field(
            description="Indicates whether the account owner has stated that this beneficiary should be trusted. This often results in reduced authentication and authorisation requirements on payments to the beneficiary."
        ),
    ] = None
    __properties = ["id", "reference", "payee", "trusted"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Beneficiary":
        """Create an instance of Beneficiary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payee
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "Beneficiary":
        """Create an instance of Beneficiary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Beneficiary.model_validate(obj)

        return Beneficiary.model_validate(
            {
                "id": obj.get("id"),
                "reference": obj.get("reference"),
                "payee": BeneficiaryPayee.from_dict(obj.get("payee")) if obj.get("payee") is not None else None,
                "trusted": obj.get("trusted"),
            }
        )
