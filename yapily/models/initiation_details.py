from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.payee import Payee
from yapily.models.payer import Payer
from typing import Set
from typing_extensions import Self


class InitiationDetails(BaseModel):
    reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The payment reference or description. Limited to a maximum of 18 characters long.",
    )
    payer: Optional[Payer] = None
    payee: Optional[Payee] = None
    __properties: ClassVar[List[str]] = ["reference", "payer", "payee"]
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
        if self.payer:
            _dict["payer"] = self.payer.to_dict()
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
                "reference": obj.get("reference"),
                "payer": Payer.from_dict(obj["payer"])
                if obj.get("payer") is not None
                else None,
                "payee": Payee.from_dict(obj["payee"])
                if obj.get("payee") is not None
                else None,
            }
        )
        return _obj
