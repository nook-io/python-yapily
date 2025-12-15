from __future__ import annotations
import pprint
import json
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from yapily.models.monitoring_status_enum import MonitoringStatusEnum


class MonitoringEndpointStatus(BaseModel):
    last_tested: Optional[datetime] = Field(None, alias="lastTested")
    resource_endpoint: Optional[StrictStr] = Field(None, alias="resourceEndpoint")
    span: Optional[StrictStr] = None
    status: Optional[MonitoringStatusEnum] = None
    __properties = ["lastTested", "resourceEndpoint", "span", "status"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MonitoringEndpointStatus:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MonitoringEndpointStatus:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return MonitoringEndpointStatus.parse_obj(obj)
        _obj = MonitoringEndpointStatus.parse_obj(
            {
                "last_tested": obj.get("lastTested"),
                "resource_endpoint": obj.get("resourceEndpoint"),
                "span": obj.get("span"),
                "status": obj.get("status"),
            }
        )
        return _obj
