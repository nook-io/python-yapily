from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution_consent import InstitutionConsent
from typing import Set
from typing_extensions import Self


class ApplicationUser(BaseModel):
    uuid: Optional[StrictStr] = Field(
        default=None,
        description="A unique identifier for the 'User' assigned by Yapily.",
    )
    application_uuid: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the application the user is associated with.",
        alias="applicationUuid",
    )
    application_user_id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. The user-friendly reference to the `User`.",
        alias="applicationUserId",
    )
    reference_id: Optional[StrictStr] = Field(default=None, alias="referenceId")
    created_at: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the user was created.",
        alias="createdAt",
    )
    institution_consents: Optional[List[InstitutionConsent]] = Field(
        default=None, alias="institutionConsents"
    )
    __properties: ClassVar[List[str]] = [
        "uuid",
        "applicationUuid",
        "applicationUserId",
        "referenceId",
        "createdAt",
        "institutionConsents",
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
        if self.institution_consents:
            for _item_institution_consents in self.institution_consents:
                if _item_institution_consents:
                    _items.append(_item_institution_consents.to_dict())
            _dict["institutionConsents"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "uuid": obj.get("uuid"),
                "applicationUuid": obj.get("applicationUuid"),
                "applicationUserId": obj.get("applicationUserId"),
                "referenceId": obj.get("referenceId"),
                "createdAt": obj.get("createdAt"),
                "institutionConsents": [
                    InstitutionConsent.from_dict(_item)
                    for _item in obj["institutionConsents"]
                ]
                if obj.get("institutionConsents") is not None
                else None,
            }
        )
        return _obj
