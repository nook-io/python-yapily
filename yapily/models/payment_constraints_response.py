from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.payment_type_of_constraints import PaymentTypeOfConstraints
from yapily.models.request_constraints import RequestConstraints
from typing import Set
from typing_extensions import Self


class PaymentConstraintsResponse(BaseModel):
    institution_id: StrictStr = Field(
        description="The id to represent the `Institution`.", alias="institutionId"
    )
    institution_country_code: Optional[StrictStr] = Field(
        default=None,
        description="2 letter ISO Country code of the `Institution`.",
        alias="institutionCountryCode",
    )
    endpoint_path: Optional[StrictStr] = Field(
        default=None,
        description="Define the applicable API end point.",
        alias="endpointPath",
    )
    endpoint_method: Optional[StrictStr] = Field(
        default=None,
        description="Https Method for the endpoint.",
        alias="endpointMethod",
    )
    payment_type: PaymentTypeOfConstraints = Field(alias="paymentType")
    request: RequestConstraints
    __properties: ClassVar[List[str]] = [
        "institutionId",
        "institutionCountryCode",
        "endpointPath",
        "endpointMethod",
        "paymentType",
        "request",
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
        if self.request:
            _dict["request"] = self.request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "institutionId": obj.get("institutionId"),
                "institutionCountryCode": obj.get("institutionCountryCode"),
                "endpointPath": obj.get("endpointPath"),
                "endpointMethod": obj.get("endpointMethod"),
                "paymentType": obj.get("paymentType"),
                "request": RequestConstraints.from_dict(obj["request"])
                if obj.get("request") is not None
                else None,
            }
        )
        return _obj
