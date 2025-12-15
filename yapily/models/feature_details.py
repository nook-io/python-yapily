from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.feature_enum import FeatureEnum
from typing import Set
from typing_extensions import Self


class FeatureDetails(BaseModel):
    feature: Optional[FeatureEnum] = None
    endpoint: Optional[StrictStr] = Field(
        default=None,
        description="Endpoints that are associated with the feature e.g. (available for use if an Institution supports a feature).",
    )
    documentation_url: Optional[StrictStr] = Field(
        default=None,
        description="The link to further documentation regarding the feature.",
        alias="documentationUrl",
    )
    __properties: ClassVar[List[str]] = ["feature", "endpoint", "documentationUrl"]
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
                "feature": obj.get("feature"),
                "endpoint": obj.get("endpoint"),
                "documentationUrl": obj.get("documentationUrl"),
            }
        )
        return _obj
