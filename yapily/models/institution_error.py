from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class InstitutionError(BaseModel):
    error_message: Optional[StrictStr] = Field(
        default=None,
        description="Textual description of the `Institution` error.",
        alias="errorMessage",
    )
    http_status_code: Optional[StrictInt] = Field(
        default=None,
        description="Numeric HTTP status code associated with the `Institution` error.",
        alias="httpStatusCode",
    )
    __properties: ClassVar[List[str]] = ["errorMessage", "httpStatusCode"]
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "errorMessage": obj.get("errorMessage"),
                "httpStatusCode": obj.get("httpStatusCode"),
            }
        )
        return _obj
