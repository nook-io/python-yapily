from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from yapily.models.delete_status_enum import DeleteStatusEnum
from typing import Optional, Set
from typing_extensions import Self


class EventSubscriptionDeleteResponse(BaseModel):
    event_type_id: StrictStr = Field(
        description="Unique identifier of the event type (for which notifications will be sent)",
        alias="eventTypeId",
    )
    application_id: StrictStr = Field(
        description="Application related to event subscription.", alias="applicationId"
    )
    created: datetime = Field(description="Creation datetime of event subscription.")
    delete_status: DeleteStatusEnum = Field(alias="deleteStatus")
    __properties: ClassVar[List[str]] = [
        "eventTypeId",
        "applicationId",
        "created",
        "deleteStatus",
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
                "eventTypeId": obj.get("eventTypeId"),
                "applicationId": obj.get("applicationId"),
                "created": obj.get("created"),
                "deleteStatus": obj.get("deleteStatus"),
            }
        )
        return _obj
