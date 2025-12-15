from __future__ import annotations
import pprint
import json
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr


class PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner(
    BaseModel
):
    type: Optional[StrictStr] = None
    code: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="A 5 digit error code"
    )
    message: Optional[StrictStr] = None
    __properties = ["type", "code", "message"]

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
    ) -> PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.parse_obj(
                obj
            )
        _obj = PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.parse_obj(
            {
                "type": obj.get("type"),
                "code": obj.get("code"),
                "message": obj.get("message"),
            }
        )
        return _obj
