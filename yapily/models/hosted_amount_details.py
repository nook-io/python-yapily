from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class HostedAmountDetails(BaseModel):
    amount_to_pay: Union[
        Annotated[float, Field(strict=True, ge=0.01)],
        Annotated[int, Field(strict=True, ge=1)],
    ] = Field(description="The payment amount", alias="amountToPay")
    currency: StrictStr = Field(
        description="The [ISO 4217](https://www.xe.com/iso4217.php) currency code"
    )
    __properties: ClassVar[List[str]] = ["amountToPay", "currency"]
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
            {"amountToPay": obj.get("amountToPay"), "currency": obj.get("currency")}
        )
        return _obj
