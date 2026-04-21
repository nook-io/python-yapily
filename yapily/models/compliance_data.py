import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.compliance_data_payer import ComplianceDataPayer


class ComplianceData(BaseModel):
    """
    __Conditional__. Information needed to complete compliance checks. Mandatory for Yapily Connect customers.  # noqa: E501
    """

    payer: ComplianceDataPayer | None = None
    __properties = ["payer"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ComplianceData":
        """Create an instance of ComplianceData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ComplianceData":
        """Create an instance of ComplianceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceData.parse_obj(obj)

        return ComplianceData.parse_obj(
            {"payer": ComplianceDataPayer.from_dict(obj.get("payer")) if obj.get("payer") is not None else None}
        )
