from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.hosted_payment_iso_status import HostedPaymentIsoStatus
from yapily.models.payment_status import PaymentStatus
from typing import Set
from typing_extensions import Self


class HostedPaymentStatusDetails(BaseModel):
    status: Optional[PaymentStatus] = None
    status_update_date: Optional[datetime] = Field(
        default=None,
        description="Date and time the status was updated.",
        alias="statusUpdateDate",
    )
    iso_status: Optional[HostedPaymentIsoStatus] = Field(
        default=None, alias="isoStatus"
    )
    __properties: ClassVar[List[str]] = ["status", "statusUpdateDate", "isoStatus"]
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
        if self.iso_status:
            _dict["isoStatus"] = self.iso_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "status": obj.get("status"),
                "statusUpdateDate": obj.get("statusUpdateDate"),
                "isoStatus": HostedPaymentIsoStatus.from_dict(obj["isoStatus"])
                if obj.get("isoStatus") is not None
                else None,
            }
        )
        return _obj
