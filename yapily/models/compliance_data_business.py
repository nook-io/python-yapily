import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.compliance_data_address import ComplianceDataAddress


class ComplianceDataBusiness(BaseModel):
    """
    __Conditional__. Mandatory if the type is BUSINESS.  # noqa: E501
    """

    name: Annotated[StrictStr, Field(description="This is the registered company name of your end user.")]
    registration_number: Annotated[
        StrictStr,
        Field(alias="registrationNumber", description="This is the registered company number of the business."),
    ]
    registered_address: Annotated[ComplianceDataAddress, Field(alias="registeredAddress")]
    trading_address: Annotated[ComplianceDataAddress | None, Field(alias="tradingAddress")] = None
    __properties = ["name", "registrationNumber", "registeredAddress", "tradingAddress"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ComplianceDataBusiness":
        """Create an instance of ComplianceDataBusiness from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of registered_address
        if self.registered_address:
            _dict["registeredAddress"] = self.registered_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trading_address
        if self.trading_address:
            _dict["tradingAddress"] = self.trading_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ComplianceDataBusiness":
        """Create an instance of ComplianceDataBusiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataBusiness.model_validate(obj)

        return ComplianceDataBusiness.model_validate(
            {
                "name": obj.get("name"),
                "registration_number": obj.get("registrationNumber"),
                "registered_address": ComplianceDataAddress.from_dict(obj.get("registeredAddress"))
                if obj.get("registeredAddress") is not None
                else None,
                "trading_address": ComplianceDataAddress.from_dict(obj.get("tradingAddress"))
                if obj.get("tradingAddress") is not None
                else None,
            }
        )
