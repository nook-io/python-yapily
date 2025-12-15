from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.enriched_historic_balance import EnrichedHistoricBalance
from yapily.models.enriched_predicted_balance import EnrichedPredictedBalance
from typing import Set
from typing_extensions import Self


class EnrichedBalances(BaseModel):
    account_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of Account Ids used to generate Balance Prediction Profile.",
        alias="accountIds",
    )
    institutions: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of Institution Ids associated with the accounts used to generate Balance Prediction Profile.",
    )
    historic: Optional[List[EnrichedHistoricBalance]] = Field(
        default=None,
        description="A list of historic balances. Each balance in the list is an aggregation (sum) of the reported balance for each account within the profile at a point in time.",
    )
    predicted: Optional[List[EnrichedPredictedBalance]] = Field(
        default=None,
        description="A list of predicted balances. Each balance in the list is a projected balance of the profile at a future point in time.",
    )
    __properties: ClassVar[List[str]] = [
        "accountIds",
        "institutions",
        "historic",
        "predicted",
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
        _items = []
        if self.historic:
            for _item_historic in self.historic:
                if _item_historic:
                    _items.append(_item_historic.to_dict())
            _dict["historic"] = _items
        _items = []
        if self.predicted:
            for _item_predicted in self.predicted:
                if _item_predicted:
                    _items.append(_item_predicted.to_dict())
            _dict["predicted"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "accountIds": obj.get("accountIds"),
                "institutions": obj.get("institutions"),
                "historic": [
                    EnrichedHistoricBalance.from_dict(_item)
                    for _item in obj["historic"]
                ]
                if obj.get("historic") is not None
                else None,
                "predicted": [
                    EnrichedPredictedBalance.from_dict(_item)
                    for _item in obj["predicted"]
                ]
                if obj.get("predicted") is not None
                else None,
            }
        )
        return _obj
