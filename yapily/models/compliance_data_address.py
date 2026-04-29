import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ComplianceDataAddress(BaseModel):
    """
    This is the registered company or trading address of your end user.  # noqa: E501
    """

    address_line1: Annotated[
        StrictStr, Field(alias="addressLine1", description="__Mandatory__. AddressLine1 of the business.")
    ]
    address_line2: Annotated[
        StrictStr | None, Field(alias="addressLine2", description="__Optional__. AddressLine2 of the business.")
    ] = None
    town_name: Annotated[StrictStr, Field(alias="townName", description="__Mandatory__. Town name of the business.")]
    post_code: Annotated[StrictStr, Field(alias="postCode", description="__Mandatory__. Post code of the business.")]
    country: Annotated[StrictStr, Field(description="__Mandatory__. Country of the business.")]
    __properties = ["addressLine1", "addressLine2", "townName", "postCode", "country"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ComplianceDataAddress":
        """Create an instance of ComplianceDataAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ComplianceDataAddress":
        """Create an instance of ComplianceDataAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceDataAddress.model_validate(obj)

        return ComplianceDataAddress.model_validate(
            {
                "address_line1": obj.get("addressLine1"),
                "address_line2": obj.get("addressLine2"),
                "town_name": obj.get("townName"),
                "post_code": obj.get("postCode"),
                "country": obj.get("country"),
            }
        )
