from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class ComplianceDataAddress(BaseModel):
    address_line1: StrictStr = Field(
        description="__Mandatory__. AddressLine1 of the business.", alias="addressLine1"
    )
    address_line2: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. AddressLine2 of the business.",
        alias="addressLine2",
    )
    town_name: StrictStr = Field(
        description="__Mandatory__. Town name of the business.", alias="townName"
    )
    post_code: StrictStr = Field(
        description="__Mandatory__. Post code of the business.", alias="postCode"
    )
    country: StrictStr = Field(description="__Mandatory__. Country of the business.")
    __properties: ClassVar[List[str]] = [
        "addressLine1",
        "addressLine2",
        "townName",
        "postCode",
        "country",
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
                "addressLine1": obj.get("addressLine1"),
                "addressLine2": obj.get("addressLine2"),
                "townName": obj.get("townName"),
                "postCode": obj.get("postCode"),
                "country": obj.get("country"),
            }
        )
        return _obj
