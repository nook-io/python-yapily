from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.country import Country
from yapily.models.credentials_type import CredentialsType
from yapily.models.environment_type import EnvironmentType
from yapily.models.feature_enum import FeatureEnum
from yapily.models.media import Media
from typing import Set
from typing_extensions import Self


class Institution(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier for the `Institution`."
    )
    name: Optional[StrictStr] = Field(
        default=None, description="The friendly name of the `Institution`."
    )
    full_name: Optional[StrictStr] = Field(
        default=None,
        description="The full name of the `Institution`.",
        alias="fullName",
    )
    countries: Optional[List[Country]] = Field(
        default=None,
        description="An array of `Country` denoting which regions the `Institution` provides coverage for",
    )
    environment_type: Optional[EnvironmentType] = Field(
        default=None, alias="environmentType"
    )
    credentials_type: Optional[CredentialsType] = Field(
        default=None, alias="credentialsType"
    )
    media: Optional[List[Media]] = Field(
        default=None,
        description="Contains links to the logo and the icons for the `Institution`",
    )
    features: Optional[List[FeatureEnum]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "fullName",
        "countries",
        "environmentType",
        "credentialsType",
        "media",
        "features",
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
        if self.countries:
            for _item_countries in self.countries:
                if _item_countries:
                    _items.append(_item_countries.to_dict())
            _dict["countries"] = _items
        _items = []
        if self.media:
            for _item_media in self.media:
                if _item_media:
                    _items.append(_item_media.to_dict())
            _dict["media"] = _items
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
                "name": obj.get("name"),
                "fullName": obj.get("fullName"),
                "countries": [Country.from_dict(_item) for _item in obj["countries"]]
                if obj.get("countries") is not None
                else None,
                "environmentType": obj.get("environmentType"),
                "credentialsType": obj.get("credentialsType"),
                "media": [Media.from_dict(_item) for _item in obj["media"]]
                if obj.get("media") is not None
                else None,
                "features": obj.get("features"),
            }
        )
        return _obj
