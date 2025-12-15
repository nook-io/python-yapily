from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from yapily.models.rate_type_enum import RateTypeEnum
from typing import Set
from typing_extensions import Self


class ExchangeRateInformation(BaseModel):
    unit_currency: StrictStr = Field(
        description="__Mandatory__. The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is `GBP`.",
        alias="unitCurrency",
    )
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="__Optional__. The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.",
    )
    rate_type: RateTypeEnum = Field(alias="rateType")
    foreign_exchange_contract_reference: Optional[StrictStr] = Field(
        default=None,
        description="__Optional__. The unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.",
        alias="foreignExchangeContractReference",
    )
    __properties: ClassVar[List[str]] = [
        "unitCurrency",
        "rate",
        "rateType",
        "foreignExchangeContractReference",
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
                "unitCurrency": obj.get("unitCurrency"),
                "rate": obj.get("rate"),
                "rateType": obj.get("rateType"),
                "foreignExchangeContractReference": obj.get(
                    "foreignExchangeContractReference"
                ),
            }
        )
        return _obj
