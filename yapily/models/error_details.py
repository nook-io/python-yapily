from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.error_issue import ErrorIssue
from typing import Set
from typing_extensions import Self


class ErrorDetails(BaseModel):
    tracing_id: StrictStr = Field(
        description="Unique identifier of the request, used by Yapily for support purposes",
        alias="tracingId",
    )
    code: StrictInt = Field(
        description="Numeric HTTP status code associated with the error"
    )
    status: StrictStr = Field(description="Textual description of the HTTP status")
    support_url: Optional[StrictStr] = Field(
        default=None,
        description="Link to where further information regarding the error can be found",
        alias="supportUrl",
    )
    source: Optional[StrictStr] = Field(
        default=None,
        description="Source of the error. This may be YAPILY, the INSTITUTION, or the USER",
    )
    issues: Optional[List[ErrorIssue]] = Field(
        default=None, description="List of issues relating to the error"
    )
    __properties: ClassVar[List[str]] = [
        "tracingId",
        "code",
        "status",
        "supportUrl",
        "source",
        "issues",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        _items = []
        if self.issues:
            for _item_issues in self.issues:
                if _item_issues:
                    _items.append(_item_issues.to_dict())
            _dict["issues"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "tracingId": obj.get("tracingId"),
                "code": obj.get("code"),
                "status": obj.get("status"),
                "supportUrl": obj.get("supportUrl"),
                "source": obj.get("source"),
                "issues": [ErrorIssue.from_dict(_item) for _item in obj["issues"]]
                if obj.get("issues") is not None
                else None,
            }
        )
        return _obj
