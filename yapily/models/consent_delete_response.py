from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.delete_status_enum import DeleteStatusEnum
from typing import Set
from typing_extensions import Self


class ConsentDeleteResponse(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None,
        description="__Conditional__. User-friendly identifier of the `User` that provides authorisation. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be provided.",
    )
    delete_status: Optional[DeleteStatusEnum] = Field(
        default=None, alias="deleteStatus"
    )
    institution_id: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. The `Institution` the authorisation request is sent to.",
        alias="institutionId",
    )
    institution_consent_id: Optional[StrictStr] = Field(
        default=None,
        description="Identification of the consent at the Institution.",
        alias="institutionConsentId",
    )
    creation_date: Optional[datetime] = Field(
        default=None,
        description="Date and time of when the consent was authorised.",
        alias="creationDate",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "deleteStatus",
        "institutionId",
        "institutionConsentId",
        "creationDate",
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
                "deleteStatus": obj.get("deleteStatus"),
                "institutionId": obj.get("institutionId"),
                "institutionConsentId": obj.get("institutionConsentId"),
                "creationDate": obj.get("creationDate"),
            }
        )
        return _obj
