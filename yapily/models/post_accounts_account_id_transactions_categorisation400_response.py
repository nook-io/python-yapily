from __future__ import annotations
import pprint
import json
from typing import Optional
from pydantic import BaseModel
from yapily.models.post_accounts_account_id_transactions_categorisation400_response_error import (
    PostAccountsAccountIdTransactionsCategorisation400ResponseError,
)


class PostAccountsAccountIdTransactionsCategorisation400Response(BaseModel):
    error: Optional[PostAccountsAccountIdTransactionsCategorisation400ResponseError] = (
        None
    )
    __properties = ["error"]

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
    ) -> PostAccountsAccountIdTransactionsCategorisation400Response:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> PostAccountsAccountIdTransactionsCategorisation400Response:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisation400Response.parse_obj(
                obj
            )
        _obj = PostAccountsAccountIdTransactionsCategorisation400Response.parse_obj(
            {
                "error": PostAccountsAccountIdTransactionsCategorisation400ResponseError.from_dict(
                    obj.get("error")
                )
                if obj.get("error") is not None
                else None
            }
        )
        return _obj
