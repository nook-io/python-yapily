import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.compliance_data_business import ComplianceDataBusiness
from yapily.models.compliance_data_individual import ComplianceDataIndividual


class ComplianceDataPayer(BaseModel):
    """
    __Conditional__. Payer details required for compliance checks.  # noqa: E501
    """

    type: Annotated[
        StrictStr,
        Field(
            description="The payer type. Allowed values: INDIVIDUAL, BUSINESS. The corresponding object must be included."
        ),
    ]
    individual: ComplianceDataIndividual | None = None
    business: ComplianceDataBusiness | None = None
    __properties = ["type", "individual", "business"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ComplianceDataPayer":
        """Create an instance of ComplianceDataPayer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of individual
        if self.individual:
            _dict["individual"] = self.individual.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business
        if self.business:
            _dict["business"] = self.business.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ComplianceDataPayer":
        """Create an instance of ComplianceDataPayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataPayer.model_validate(obj)

        return ComplianceDataPayer.model_validate(
            {
                "type": obj.get("type"),
                "individual": ComplianceDataIndividual.from_dict(obj.get("individual"))
                if obj.get("individual") is not None
                else None,
                "business": ComplianceDataBusiness.from_dict(obj.get("business"))
                if obj.get("business") is not None
                else None,
            }
        )
