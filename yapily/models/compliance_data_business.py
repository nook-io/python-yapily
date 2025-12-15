from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.compliance_data_address import ComplianceDataAddress
from typing import Set
from typing_extensions import Self


class ComplianceDataBusiness(BaseModel):
    name: StrictStr = Field(
        description="This is the registered company name of your end user."
    )
    registration_number: StrictStr = Field(
        description="This is the registered company number of the business.",
        alias="registrationNumber",
    )
    registered_address: ComplianceDataAddress = Field(alias="registeredAddress")
    trading_address: Optional[ComplianceDataAddress] = Field(
        default=None, alias="tradingAddress"
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "registrationNumber",
        "registeredAddress",
        "tradingAddress",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.registered_address:
            _dict["registeredAddress"] = self.registered_address.to_dict()
        if self.trading_address:
            _dict["tradingAddress"] = self.trading_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "registrationNumber": obj.get("registrationNumber"),
                "registeredAddress": ComplianceDataAddress.from_dict(
                    obj["registeredAddress"]
                )
                if obj.get("registeredAddress") is not None
                else None,
                "tradingAddress": ComplianceDataAddress.from_dict(obj["tradingAddress"])
                if obj.get("tradingAddress") is not None
                else None,
            }
        )
        return _obj
