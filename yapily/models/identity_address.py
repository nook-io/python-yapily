# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from yapily.models.address_type_enum import AddressTypeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IdentityAddress(BaseModel):
    """
    IdentityAddress
    """ # noqa: E501
    address_lines: Optional[List[StrictStr]] = Field(default=None, alias="addressLines")
    city: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country: Optional[StrictStr] = None
    street_name: Optional[StrictStr] = Field(default=None, alias="streetName")
    building_number: Optional[StrictStr] = Field(default=None, alias="buildingNumber")
    type: Optional[AddressTypeEnum] = None
    county: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["addressLines", "city", "postalCode", "country", "streetName", "buildingNumber", "type", "county"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdentityAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IdentityAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLines": obj.get("addressLines"),
            "city": obj.get("city"),
            "postalCode": obj.get("postalCode"),
            "country": obj.get("country"),
            "streetName": obj.get("streetName"),
            "buildingNumber": obj.get("buildingNumber"),
            "type": obj.get("type"),
            "county": obj.get("county")
        })
        return _obj


