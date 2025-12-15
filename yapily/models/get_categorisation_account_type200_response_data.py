from __future__ import annotations
import pprint
import json
from typing import Optional
from pydantic import BaseModel, StrictStr, conlist


class GetCategorisationAccountType200ResponseData(BaseModel):
    incoming: Optional[conlist(StrictStr)] = None
    outgoing: Optional[conlist(StrictStr)] = None
    __properties = ["incoming", "outgoing"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetCategorisationAccountType200ResponseData:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetCategorisationAccountType200ResponseData:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return GetCategorisationAccountType200ResponseData.parse_obj(obj)
        _obj = GetCategorisationAccountType200ResponseData.parse_obj(
            {"incoming": obj.get("incoming"), "outgoing": obj.get("outgoing")}
        )
        return _obj
