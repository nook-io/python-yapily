import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.delete_status_enum import DeleteStatusEnum


class EventSubscriptionDeleteResponse(BaseModel):
    """
    EventSubscriptionDeleteResponse
    """

    event_type_id: Annotated[
        StrictStr,
        Field(
            alias="eventTypeId",
            description="Unique identifier of the event type (for which notifications will be sent)",
        ),
    ]
    application_id: Annotated[
        StrictStr, Field(alias="applicationId", description="Application related to event subscription.")
    ]
    created: Annotated[datetime, Field(description="Creation datetime of event subscription.")]
    delete_status: Annotated[DeleteStatusEnum, Field(alias="deleteStatus")]
    __properties = ["eventTypeId", "applicationId", "created", "deleteStatus"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EventSubscriptionDeleteResponse":
        """Create an instance of EventSubscriptionDeleteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "EventSubscriptionDeleteResponse":
        """Create an instance of EventSubscriptionDeleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventSubscriptionDeleteResponse.model_validate(obj)

        return EventSubscriptionDeleteResponse.model_validate(
            {
                "event_type_id": obj.get("eventTypeId"),
                "application_id": obj.get("applicationId"),
                "created": obj.get("created"),
                "delete_status": obj.get("deleteStatus"),
            }
        )
