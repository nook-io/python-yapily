import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.enriched_wrapper import EnrichedWrapper
from yapily.models.profile_consent import ProfileConsent


class FinancialProfile(BaseModel):
    """
    A financial profile for a User.  # noqa: E501
    """

    status: Annotated[
        StrictStr | None, Field(description="The status, can be EMPTY, PARTIAL, PENDING, COMPLETED or ERROR.")
    ] = None
    profile_consents: Annotated[
        list[ProfileConsent] | None,
        Field(alias="profileConsents", description="A list of ProfileConsent used in the financial profile."),
    ] = None
    enrichment: EnrichedWrapper | None = None
    __properties = ["status", "profileConsents", "enrichment"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FinancialProfile":
        """Create an instance of FinancialProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of enrichment
        if self.enrichment:
            _dict["enrichment"] = self.enrichment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "FinancialProfile":
        """Create an instance of FinancialProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FinancialProfile.model_validate(obj)

        return FinancialProfile.model_validate(
            {
                "status": obj.get("status"),
                "profile_consents": [ProfileConsent.from_dict(_item) for _item in obj.get("profileConsents")]
                if obj.get("profileConsents") is not None
                else None,
                "enrichment": EnrichedWrapper.from_dict(obj.get("enrichment"))
                if obj.get("enrichment") is not None
                else None,
            }
        )
