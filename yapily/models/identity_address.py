from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.address_type_enum import AddressTypeEnum
from typing import Set
from typing_extensions import Self


class IdentityAddress(BaseModel):
    address_lines: Optional[List[StrictStr]] = Field(default=None, alias="addressLines")
    city: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country: Optional[StrictStr] = None
    street_name: Optional[StrictStr] = Field(default=None, alias="streetName")
    building_number: Optional[StrictStr] = Field(default=None, alias="buildingNumber")
    type: Optional[AddressTypeEnum] = None
    county: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "addressLines",
        "city",
        "postalCode",
        "country",
        "streetName",
        "buildingNumber",
        "type",
        "county",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "addressLines": obj.get("addressLines"),
                "city": obj.get("city"),
                "postalCode": obj.get("postalCode"),
                "country": obj.get("country"),
                "streetName": obj.get("streetName"),
                "buildingNumber": obj.get("buildingNumber"),
                "type": obj.get("type"),
                "county": obj.get("county"),
            }
        )
        return _obj
