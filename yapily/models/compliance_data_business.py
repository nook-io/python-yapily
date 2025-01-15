# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 7.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.compliance_data_address import ComplianceDataAddress
from typing import Optional, Set
from typing_extensions import Self

class ComplianceDataBusiness(BaseModel):
    """
    __Conditional__. Mandatory if the type is BUSINESS.
    """ # noqa: E501
    name: StrictStr = Field(description="This is the registered company name of your end user.")
    registration_number: StrictStr = Field(description="This is the registered company number of the business.", alias="registrationNumber")
    registered_address: ComplianceDataAddress = Field(alias="registeredAddress")
    trading_address: Optional[ComplianceDataAddress] = Field(default=None, alias="tradingAddress")
    __properties: ClassVar[List[str]] = ["name", "registrationNumber", "registeredAddress", "tradingAddress"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ComplianceDataBusiness from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of registered_address
        if self.registered_address:
            _dict['registeredAddress'] = self.registered_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trading_address
        if self.trading_address:
            _dict['tradingAddress'] = self.trading_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComplianceDataBusiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "registrationNumber": obj.get("registrationNumber"),
            "registeredAddress": ComplianceDataAddress.from_dict(obj["registeredAddress"]) if obj.get("registeredAddress") is not None else None,
            "tradingAddress": ComplianceDataAddress.from_dict(obj["tradingAddress"]) if obj.get("tradingAddress") is not None else None
        })
        return _obj


