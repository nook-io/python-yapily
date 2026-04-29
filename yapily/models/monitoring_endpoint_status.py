import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.monitoring_status_enum import MonitoringStatusEnum


class MonitoringEndpointStatus(BaseModel):
    """
    MonitoringEndpointStatus
    """

    last_tested: Annotated[datetime | None, Field(alias="lastTested")] = None
    resource_endpoint: Annotated[StrictStr | None, Field(alias="resourceEndpoint")] = None
    span: StrictStr | None = None
    status: MonitoringStatusEnum | None = None
    __properties = ["lastTested", "resourceEndpoint", "span", "status"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "MonitoringEndpointStatus":
        """Create an instance of MonitoringEndpointStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "MonitoringEndpointStatus":
        """Create an instance of MonitoringEndpointStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MonitoringEndpointStatus.model_validate(obj)

        return MonitoringEndpointStatus.model_validate(
            {
                "last_tested": obj.get("lastTested"),
                "resource_endpoint": obj.get("resourceEndpoint"),
                "span": obj.get("span"),
                "status": obj.get("status"),
            }
        )
