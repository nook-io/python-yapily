from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution_error import InstitutionError
from typing import Set
from typing_extensions import Self


class ErrorIssue(BaseModel):
    type: StrictStr = Field(description="Category of the issue")
    code: StrictStr = Field(
        description="Code that uniquely identifies the type of issue"
    )
    parameter: Optional[StrictStr] = Field(
        default=None,
        description="Identfies the parameter / property within the request (headers, query parameters or body) that the issue relates to. For headers and query parameters, it refers to the parameter name. For the body, it refers to the JSONPath of the property",
    )
    message: Optional[StrictStr] = Field(
        default=None,
        description="Human readable description of the issue that was experienced",
    )
    institution_error: Optional[InstitutionError] = Field(
        default=None, alias="institutionError"
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "code",
        "parameter",
        "message",
        "institutionError",
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
        if self.institution_error:
            _dict["institutionError"] = self.institution_error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "code": obj.get("code"),
                "parameter": obj.get("parameter"),
                "message": obj.get("message"),
                "institutionError": InstitutionError.from_dict(obj["institutionError"])
                if obj.get("institutionError") is not None
                else None,
            }
        )
        return _obj
