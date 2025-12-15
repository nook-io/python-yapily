from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.enriched_balances import EnrichedBalances
from yapily.models.profile_consent import ProfileConsent
from typing import Set
from typing_extensions import Self


class BalancePredictionProfile(BaseModel):
    status: Optional[StrictStr] = Field(
        default=None,
        description="The status, will be COMPLETED which represents successful retreival of profile.",
    )
    profile_consents: Optional[List[ProfileConsent]] = Field(
        default=None,
        description="A list of ProfileConsents used in the Balance Prediction profile.",
        alias="profileConsents",
    )
    enriched_balances: Optional[List[EnrichedBalances]] = Field(
        default=None,
        description="A list of Balances returned by Balance Prediction profile.",
        alias="enrichedBalances",
    )
    __properties: ClassVar[List[str]] = [
        "status",
        "profileConsents",
        "enrichedBalances",
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
        _items = []
        if self.profile_consents:
            for _item_profile_consents in self.profile_consents:
                if _item_profile_consents:
                    _items.append(_item_profile_consents.to_dict())
            _dict["profileConsents"] = _items
        _items = []
        if self.enriched_balances:
            for _item_enriched_balances in self.enriched_balances:
                if _item_enriched_balances:
                    _items.append(_item_enriched_balances.to_dict())
            _dict["enrichedBalances"] = _items
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
                "enrichedBalances": [
                    EnrichedBalances.from_dict(_item)
                    for _item in obj["enrichedBalances"]
                ]
                if obj.get("enrichedBalances") is not None
                else None,
            }
        )
        return _obj
