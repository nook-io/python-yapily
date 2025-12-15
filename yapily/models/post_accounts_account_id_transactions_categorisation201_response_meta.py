from __future__ import annotations
import pprint
import json
from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class PostAccountsAccountIdTransactionsCategorisation201ResponseMeta(BaseModel):
    tracing_id: Optional[StrictStr] = Field(None, alias="tracingId")
    __properties = ["tracingId"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> PostAccountsAccountIdTransactionsCategorisation201ResponseMeta:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> PostAccountsAccountIdTransactionsCategorisation201ResponseMeta:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisation201ResponseMeta.parse_obj(
                obj
            )
        _obj = PostAccountsAccountIdTransactionsCategorisation201ResponseMeta.parse_obj(
            {"tracing_id": obj.get("tracingId")}
        )
        return _obj
