from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from yapily.models.notification import Notification
from typing import Optional, Set
from typing_extensions import Self


class EventSubscriptionRequest(BaseModel):
    event_type_id: StrictStr = Field(
        description="Unique identifier of the event type (for which notifications will be sent).<br><br>Allowed values: payment.status, payment.status.completed, payment.isoStatus ",
        alias="eventTypeId",
    )
    notification: Notification
    __properties: ClassVar[List[str]] = ["eventTypeId", "notification"]
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
        if self.notification:
            _dict["notification"] = self.notification.to_dict()
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
                "notification": Notification.from_dict(obj["notification"])
                if obj.get("notification") is not None
                else None,
            }
        )
        return _obj
