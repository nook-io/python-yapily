from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.beneficiary_payee import BeneficiaryPayee
from typing import Set
from typing_extensions import Self


class Beneficiary(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the `beneficiary`."
    )
    reference: Optional[StrictStr] = Field(
        default=None,
        description="A creditor reference that is requested to be used for all payment instructions to this beneficiary.",
    )
    payee: Optional[BeneficiaryPayee] = None
    trusted: Optional[StrictBool] = Field(
        default=None,
        description="Indicates whether the account owner has stated that this beneficiary should be trusted. This often results in reduced authentication and authorisation requirements on payments to the beneficiary.",
    )
    __properties: ClassVar[List[str]] = ["id", "reference", "payee", "trusted"]
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
        if self.payee:
            _dict["payee"] = self.payee.to_dict()
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
                "reference": obj.get("reference"),
                "payee": BeneficiaryPayee.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
                "trusted": obj.get("trusted"),
            }
        )
        return _obj
