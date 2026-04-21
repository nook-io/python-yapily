import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.monitoring_status_enum import MonitoringStatusEnum


class MonitoringFeatureStatus(BaseModel):
    """
    MonitoringFeatureStatus
    """

    last_tested: Annotated[datetime | None, Field(alias="lastTested")] = None
    span: StrictStr | None = None
    status: MonitoringStatusEnum | None = None
    __properties = ["lastTested", "span", "status"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "MonitoringFeatureStatus":
        """Create an instance of MonitoringFeatureStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "MonitoringFeatureStatus":
        """Create an instance of MonitoringFeatureStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MonitoringFeatureStatus.parse_obj(obj)

        return MonitoringFeatureStatus.parse_obj(
            {"last_tested": obj.get("lastTested"), "span": obj.get("span"), "status": obj.get("status")}
        )
