from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class ProfileConsent(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the `consent` in context of a user's profile.",
    )
    status: Optional[StrictStr] = Field(
        default=None, description="The status, can be PENDING, COMPLETED or ERROR."
    )
    user_id: Optional[StrictStr] = Field(
        default=None, description="The userUuid.", alias="userId"
    )
    reference_consent_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the consent.",
        alias="referenceConsentId",
    )
    institution_id: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. The  `Institution` the authorisation request is sent to.",
        alias="institutionId",
    )
    created_at: Optional[datetime] = Field(
        default=None,
        description="When a profile consent is created.",
        alias="createdAt",
    )
    expires_at: Optional[datetime] = Field(
        default=None,
        description="When a profile consent is expired after created + X.",
        alias="expiresAt",
    )
    data_inserted_at: Optional[datetime] = Field(
        default=None,
        description="After data retrieval from aggregated profile consent is completed.",
        alias="dataInsertedAt",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "status",
        "userId",
        "referenceConsentId",
        "institutionId",
        "createdAt",
        "expiresAt",
        "dataInsertedAt",
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
                "id": obj.get("id"),
                "status": obj.get("status"),
                "userId": obj.get("userId"),
                "referenceConsentId": obj.get("referenceConsentId"),
                "institutionId": obj.get("institutionId"),
                "createdAt": obj.get("createdAt"),
                "expiresAt": obj.get("expiresAt"),
                "dataInsertedAt": obj.get("dataInsertedAt"),
            }
        )
        return _obj
