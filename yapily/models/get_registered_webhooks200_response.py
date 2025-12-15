from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.get_registered_webhooks200_response_data import (
    GetRegisteredWebhooks200ResponseData,
)
from yapily.models.metadata import Metadata
from typing import Set
from typing_extensions import Self


class GetRegisteredWebhooks200Response(BaseModel):
    metadata: Optional[Metadata] = None
    data: Optional[GetRegisteredWebhooks200ResponseData] = None
    __properties: ClassVar[List[str]] = ["metadata", "data"]
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
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        if self.data:
            _dict["data"] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "metadata": Metadata.from_dict(obj["metadata"])
                if obj.get("metadata") is not None
                else None,
                "data": GetRegisteredWebhooks200ResponseData.from_dict(obj["data"])
                if obj.get("data") is not None
                else None,
            }
        )
        return _obj
