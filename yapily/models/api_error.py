from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.institution_error import InstitutionError
from typing import Set
from typing_extensions import Self


class ApiError(BaseModel):
    code: Optional[StrictInt] = Field(
        default=None,
        description="_Mandatory_. Numeric `HTTP` status code associated with the error.",
    )
    institution_error: Optional[InstitutionError] = Field(
        default=None, alias="institutionError"
    )
    message: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. Description of the exact error that has been experienced.",
    )
    source: Optional[StrictStr] = None
    status: Optional[StrictStr] = Field(
        default=None,
        description="__Mandatory__. Textual description of the `HTTP` error status type.",
    )
    tracing_id: Optional[StrictStr] = Field(
        default=None,
        description="_Optional_.  A unique identifier assigned by Yapily for the request that can be used for support purposes.",
        alias="tracingId",
    )
    __properties: ClassVar[List[str]] = [
        "code",
        "institutionError",
        "message",
        "source",
        "status",
        "tracingId",
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
                "code": obj.get("code"),
                "institutionError": InstitutionError.from_dict(obj["institutionError"])
                if obj.get("institutionError") is not None
                else None,
                "message": obj.get("message"),
                "source": obj.get("source"),
                "status": obj.get("status"),
                "tracingId": obj.get("tracingId"),
            }
        )
        return _obj
