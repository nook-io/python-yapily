from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.multi_authorisation import MultiAuthorisation
from yapily.models.payment_iso_status import PaymentIsoStatus
from yapily.models.payment_status import PaymentStatus
from typing import Set
from typing_extensions import Self


class PaymentStatusDetails(BaseModel):
    status: Optional[PaymentStatus] = None
    status_reason: Optional[StrictStr] = Field(default=None, alias="statusReason")
    status_reason_description: Optional[StrictStr] = Field(
        default=None, alias="statusReasonDescription"
    )
    status_update_date: Optional[datetime] = Field(
        default=None, alias="statusUpdateDate"
    )
    multi_authorisation_status: Optional[MultiAuthorisation] = Field(
        default=None, alias="multiAuthorisationStatus"
    )
    iso_status: Optional[PaymentIsoStatus] = Field(default=None, alias="isoStatus")
    __properties: ClassVar[List[str]] = [
        "status",
        "statusReason",
        "statusReasonDescription",
        "statusUpdateDate",
        "multiAuthorisationStatus",
        "isoStatus",
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
        if self.multi_authorisation_status:
            _dict["multiAuthorisationStatus"] = (
                self.multi_authorisation_status.to_dict()
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
                "statusReason": obj.get("statusReason"),
                "statusReasonDescription": obj.get("statusReasonDescription"),
                "statusUpdateDate": obj.get("statusUpdateDate"),
                "multiAuthorisationStatus": MultiAuthorisation.from_dict(
                    obj["multiAuthorisationStatus"]
                )
                if obj.get("multiAuthorisationStatus") is not None
                else None,
                "isoStatus": PaymentIsoStatus.from_dict(obj["isoStatus"])
                if obj.get("isoStatus") is not None
                else None,
            }
        )
        return _obj
