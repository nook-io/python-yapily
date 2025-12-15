from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.get_bulk_payment_status200_response_data import (
    GetBulkPaymentStatus200ResponseData,
)
from yapily.models.get_bulk_payment_status200_response_meta import (
    GetBulkPaymentStatus200ResponseMeta,
)
from typing import Set
from typing_extensions import Self


class GetBulkPaymentStatus200Response(BaseModel):
    meta: Optional[GetBulkPaymentStatus200ResponseMeta] = None
    data: Optional[GetBulkPaymentStatus200ResponseData] = None
    __properties: ClassVar[List[str]] = ["meta", "data"]
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
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
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
                "meta": GetBulkPaymentStatus200ResponseMeta.from_dict(obj["meta"])
                if obj.get("meta") is not None
                else None,
                "data": GetBulkPaymentStatus200ResponseData.from_dict(obj["data"])
                if obj.get("data") is not None
                else None,
            }
        )
        return _obj
