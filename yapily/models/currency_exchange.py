from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self


class CurrencyExchange(BaseModel):
    source_currency: Optional[StrictStr] = Field(
        default=None,
        description="Currency from which an amount is to be converted.",
        alias="sourceCurrency",
    )
    target_currency: Optional[StrictStr] = Field(
        default=None,
        description="Currency to which an amount is to be converted.",
        alias="targetCurrency",
    )
    unit_currency: Optional[StrictStr] = Field(
        default=None,
        description="The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.",
        alias="unitCurrency",
    )
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.",
        alias="exchangeRate",
    )
    __properties: ClassVar[List[str]] = [
        "sourceCurrency",
        "targetCurrency",
        "unitCurrency",
        "exchangeRate",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "sourceCurrency": obj.get("sourceCurrency"),
                "targetCurrency": obj.get("targetCurrency"),
                "unitCurrency": obj.get("unitCurrency"),
                "exchangeRate": obj.get("exchangeRate"),
            }
        )
        return _obj
