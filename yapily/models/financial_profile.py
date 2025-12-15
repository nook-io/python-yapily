from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.enriched_wrapper import EnrichedWrapper
from yapily.models.profile_consent import ProfileConsent
from typing import Set
from typing_extensions import Self


class FinancialProfile(BaseModel):
    status: Optional[StrictStr] = Field(
        default=None,
        description="The status, can be EMPTY, PARTIAL, PENDING, COMPLETED or ERROR.",
    )
    profile_consents: Optional[List[ProfileConsent]] = Field(
        default=None,
        description="A list of ProfileConsent used in the financial profile.",
        alias="profileConsents",
    )
    enrichment: Optional[EnrichedWrapper] = None
    __properties: ClassVar[List[str]] = ["status", "profileConsents", "enrichment"]
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
        _items = []
        if self.profile_consents:
            for _item_profile_consents in self.profile_consents:
                if _item_profile_consents:
                    _items.append(_item_profile_consents.to_dict())
            _dict["profileConsents"] = _items
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "status": obj.get("status"),
                "profileConsents": [
                    ProfileConsent.from_dict(_item) for _item in obj["profileConsents"]
                ]
                if obj.get("profileConsents") is not None
                else None,
                "enrichment": EnrichedWrapper.from_dict(obj["enrichment"])
                if obj.get("enrichment") is not None
                else None,
            }
        )
        return _obj
