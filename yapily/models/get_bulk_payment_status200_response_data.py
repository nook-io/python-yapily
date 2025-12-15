from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.get_bulk_payment_status200_response_data_status_details import (
    GetBulkPaymentStatus200ResponseDataStatusDetails,
)
from typing import Set
from typing_extensions import Self


class GetBulkPaymentStatus200ResponseData(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the Bulk Payment"
    )
    consent_id: Optional[StrictStr] = Field(
        default=None, description="Identification of the consent.", alias="consentId"
    )
    status_details: Optional[GetBulkPaymentStatus200ResponseDataStatusDetails] = Field(
        default=None, alias="statusDetails"
    )
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    __properties: ClassVar[List[str]] = [
        "id",
        "consentId",
        "statusDetails",
        "createdAt",
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
        if self.status_details:
            _dict["statusDetails"] = self.status_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "consentId": obj.get("consentId"),
                "statusDetails": GetBulkPaymentStatus200ResponseDataStatusDetails.from_dict(
                    obj["statusDetails"]
                )
                if obj.get("statusDetails") is not None
                else None,
                "createdAt": obj.get("createdAt"),
            }
        )
        return _obj
