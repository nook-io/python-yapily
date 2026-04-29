import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.address_type_enum import AddressTypeEnum


class IdentityAddress(BaseModel):
    """
    IdentityAddress
    """

    address_lines: Annotated[list[StrictStr] | None, Field(alias="addressLines")] = None
    city: StrictStr | None = None
    postal_code: Annotated[StrictStr | None, Field(alias="postalCode")] = None
    country: StrictStr | None = None
    street_name: Annotated[StrictStr | None, Field(alias="streetName")] = None
    building_number: Annotated[StrictStr | None, Field(alias="buildingNumber")] = None
    type: AddressTypeEnum | None = None
    county: StrictStr | None = None
    __properties = ["addressLines", "city", "postalCode", "country", "streetName", "buildingNumber", "type", "county"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "IdentityAddress":
        """Create an instance of IdentityAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "IdentityAddress":
        """Create an instance of IdentityAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityAddress.model_validate(obj)

        return IdentityAddress.model_validate(
            {
                "address_lines": obj.get("addressLines"),
                "city": obj.get("city"),
                "postal_code": obj.get("postalCode"),
                "country": obj.get("country"),
                "street_name": obj.get("streetName"),
                "building_number": obj.get("buildingNumber"),
                "type": obj.get("type"),
                "county": obj.get("county"),
            }
        )
