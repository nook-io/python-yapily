# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 4.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from yapily.models.post_accounts_account_id_transactions_categorisation400_response_error_issues_inner import (
    PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner,
)


class PostAccountsAccountIdTransactionsCategorisation400ResponseError(BaseModel):
    """
    PostAccountsAccountIdTransactionsCategorisation400ResponseError
    """

    tracing_id: Optional[StrictStr] = Field(None, alias="tracingId")
    code: Optional[Union[StrictFloat, StrictInt]] = None
    status: Optional[StrictStr] = None
    support_url: Optional[StrictStr] = Field(None, alias="supportUrl")
    source: Optional[StrictStr] = None
    issues: Optional[
        conlist(
            PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner
        )
    ] = None
    __properties = ["tracingId", "code", "status", "supportUrl", "source", "issues"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> PostAccountsAccountIdTransactionsCategorisation400ResponseError:
        """Create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in issues (list)
        _items = []
        if self.issues:
            for _item in self.issues:
                if _item:
                    _items.append(_item.to_dict())
            _dict["issues"] = _items
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> PostAccountsAccountIdTransactionsCategorisation400ResponseError:
        """Create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisation400ResponseError.parse_obj(
                obj
            )

        _obj = PostAccountsAccountIdTransactionsCategorisation400ResponseError.parse_obj(
            {
                "tracing_id": obj.get("tracingId"),
                "code": obj.get("code"),
                "status": obj.get("status"),
                "support_url": obj.get("supportUrl"),
                "source": obj.get("source"),
                "issues": [
                    PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.from_dict(
                        _item
                    )
                    for _item in obj.get("issues")
                ]
                if obj.get("issues") is not None
                else None,
            }
        )
        return _obj
