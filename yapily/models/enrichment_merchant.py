from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class EnrichmentMerchant(BaseModel):
    merchant_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the indivdual merchant involved in the transaction e.g. (TESCO Petrol).",
        alias="merchantName",
    )
    parent_group: Optional[StrictStr] = Field(
        default=None,
        description="The parent organisation that the merchant belongs to e.g. (TESCO).",
        alias="parentGroup",
    )
    __properties: ClassVar[List[str]] = ["merchantName", "parentGroup"]
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
                "merchantName": obj.get("merchantName"),
                "parentGroup": obj.get("parentGroup"),
            }
        )
        return _obj
