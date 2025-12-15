from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self


class SearchApplicationsPublicFilterValuesParameter(BaseModel):
    application_ids: Optional[Annotated[List[StrictStr], Field(max_length=15)]] = Field(
        default=None,
        description="Sub-application ids to filter the results for. If provided, the results will only include sub-applications with the given ids. Non-existent ids will be ignored.",
        alias="applicationIds",
    )
    offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=0, description="The number of results to skip."
    )
    limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(
        default=1000, description="The maximum number of results to return."
    )
    sort: Optional[StrictStr] = Field(
        default="name",
        description="The field to sort the results by.<br><br>Possible values:<ul><li>`last_updated` (ascending)</li><li>`-last_updated` (descending)</li><li>`name` (ascending)</li><li>`-name` (descending)</li><li>`uuid` (ascending)</li><li>`-uuid` (descending)</li></ul>",
    )
    __properties: ClassVar[List[str]] = ["applicationIds", "offset", "limit", "sort"]
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
                "applicationIds": obj.get("applicationIds"),
                "offset": obj.get("offset") if obj.get("offset") is not None else 0,
                "limit": obj.get("limit") if obj.get("limit") is not None else 1000,
                "sort": obj.get("sort") if obj.get("sort") is not None else "name",
            }
        )
        return _obj
