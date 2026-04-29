import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.enriched_historic_balance import EnrichedHistoricBalance
from yapily.models.enriched_predicted_balance import EnrichedPredictedBalance


class EnrichedBalances(BaseModel):
    """
    Enriched Balance information generated which include historic aggregated balances and predicted balances  # noqa: E501
    """

    account_ids: Annotated[
        list[StrictStr] | None,
        Field(alias="accountIds", description="A list of Account Ids used to generate Balance Prediction Profile."),
    ] = None
    institutions: Annotated[
        list[StrictStr] | None,
        Field(
            description="A list of Institution Ids associated with the accounts used to generate Balance Prediction Profile."
        ),
    ] = None
    historic: Annotated[
        list[EnrichedHistoricBalance] | None,
        Field(
            description="A list of historic balances. Each balance in the list is an aggregation (sum) of the reported balance for each account within the profile at a point in time."
        ),
    ] = None
    predicted: Annotated[
        list[EnrichedPredictedBalance] | None,
        Field(
            description="A list of predicted balances. Each balance in the list is a projected balance of the profile at a future point in time."
        ),
    ] = None
    __properties = ["accountIds", "institutions", "historic", "predicted"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EnrichedBalances":
        """Create an instance of EnrichedBalances from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in historic (list)
        _items = []
        if self.historic:
            for _item in self.historic:
                if _item:
                    _items.append(_item.to_dict())
            _dict["historic"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in predicted (list)
        _items = []
        if self.predicted:
            for _item in self.predicted:
                if _item:
                    _items.append(_item.to_dict())
            _dict["predicted"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "EnrichedBalances":
        """Create an instance of EnrichedBalances from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedBalances.model_validate(obj)

        return EnrichedBalances.model_validate(
            {
                "account_ids": obj.get("accountIds"),
                "institutions": obj.get("institutions"),
                "historic": [EnrichedHistoricBalance.from_dict(_item) for _item in obj.get("historic")]
                if obj.get("historic") is not None
                else None,
                "predicted": [EnrichedPredictedBalance.from_dict(_item) for _item in obj.get("predicted")]
                if obj.get("predicted") is not None
                else None,
            }
        )
