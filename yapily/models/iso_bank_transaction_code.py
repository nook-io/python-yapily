import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.iso_code_details import IsoCodeDetails


class IsoBankTransactionCode(BaseModel):
    """
    Defines the underlying transaction type (e.g. Card or Debit Transactions, Loans or Mortages). <br><br> Conforms to `ISO` standards - ISO 20022.  # noqa: E501
    """

    domain_code: Annotated[IsoCodeDetails | None, Field(alias="domainCode")] = None
    family_code: Annotated[IsoCodeDetails | None, Field(alias="familyCode")] = None
    sub_family_code: Annotated[IsoCodeDetails | None, Field(alias="subFamilyCode")] = None
    __properties = ["domainCode", "familyCode", "subFamilyCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "IsoBankTransactionCode":
        """Create an instance of IsoBankTransactionCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of domain_code
        if self.domain_code:
            _dict["domainCode"] = self.domain_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of family_code
        if self.family_code:
            _dict["familyCode"] = self.family_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_family_code
        if self.sub_family_code:
            _dict["subFamilyCode"] = self.sub_family_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "IsoBankTransactionCode":
        """Create an instance of IsoBankTransactionCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IsoBankTransactionCode.parse_obj(obj)

        return IsoBankTransactionCode.parse_obj(
            {
                "domain_code": IsoCodeDetails.from_dict(obj.get("domainCode"))
                if obj.get("domainCode") is not None
                else None,
                "family_code": IsoCodeDetails.from_dict(obj.get("familyCode"))
                if obj.get("familyCode") is not None
                else None,
                "sub_family_code": IsoCodeDetails.from_dict(obj.get("subFamilyCode"))
                if obj.get("subFamilyCode") is not None
                else None,
            }
        )
