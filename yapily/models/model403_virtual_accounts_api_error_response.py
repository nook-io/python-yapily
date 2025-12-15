from __future__ import annotations
import pprint
import json
from typing import Optional
from pydantic import BaseModel, conlist
from yapily.models.error_details import ErrorDetails
from yapily.models.monitoring_endpoint_status import MonitoringEndpointStatus


class Model403VirtualAccountsApiErrorResponse(BaseModel):
    error: Optional[ErrorDetails] = None
    monitoring: Optional[conlist(MonitoringEndpointStatus)] = None
    __properties = ["error", "monitoring"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Model403VirtualAccountsApiErrorResponse:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        if self.error:
            _dict["error"] = self.error.to_dict()
        _items = []
        if self.monitoring:
            for _item in self.monitoring:
                if _item:
                    _items.append(_item.to_dict())
            _dict["monitoring"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model403VirtualAccountsApiErrorResponse:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return Model403VirtualAccountsApiErrorResponse.parse_obj(obj)
        _obj = Model403VirtualAccountsApiErrorResponse.parse_obj(
            {
                "error": ErrorDetails.from_dict(obj.get("error"))
                if obj.get("error") is not None
                else None,
                "monitoring": [
                    MonitoringEndpointStatus.from_dict(_item)
                    for _item in obj.get("monitoring")
                ]
                if obj.get("monitoring") is not None
                else None,
            }
        )
        return _obj
