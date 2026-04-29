import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.enriched_balances import EnrichedBalances
from yapily.models.profile_consent import ProfileConsent


class BalancePredictionProfile(BaseModel):
    """
    A Balance Prediction profile for a User.  # noqa: E501
    """

    status: Annotated[
        StrictStr | None,
        Field(description="The status, will be COMPLETED which represents successful retreival of profile."),
    ] = None
    profile_consents: Annotated[
        list[ProfileConsent] | None,
        Field(alias="profileConsents", description="A list of ProfileConsents used in the Balance Prediction profile."),
    ] = None
    enriched_balances: Annotated[
        list[EnrichedBalances] | None,
        Field(alias="enrichedBalances", description="A list of Balances returned by Balance Prediction profile."),
    ] = None
    __properties = ["status", "profileConsents", "enrichedBalances"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "BalancePredictionProfile":
        """Create an instance of BalancePredictionProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in profile_consents (list)
        _items = []
        if self.profile_consents:
            for _item in self.profile_consents:
                if _item:
                    _items.append(_item.to_dict())
            _dict["profileConsents"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in enriched_balances (list)
        _items = []
        if self.enriched_balances:
            for _item in self.enriched_balances:
                if _item:
                    _items.append(_item.to_dict())
            _dict["enrichedBalances"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "BalancePredictionProfile":
        """Create an instance of BalancePredictionProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BalancePredictionProfile.model_validate(obj)

        return BalancePredictionProfile.model_validate(
            {
                "status": obj.get("status"),
                "profile_consents": [ProfileConsent.from_dict(_item) for _item in obj.get("profileConsents")]
                if obj.get("profileConsents") is not None
                else None,
                "enriched_balances": [EnrichedBalances.from_dict(_item) for _item in obj.get("enrichedBalances")]
                if obj.get("enrichedBalances") is not None
                else None,
            }
        )
