from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class PostAccountsAccountIdTransactionsCategorisationRequest(BaseModel):
    country_code: StrictStr = Field(
        description="_Mandatory_, ISO 3166-1 alpha-2 two-letter country codes e.g. GB",
        alias="countryCode",
    )
    categorisation_type: StrictStr = Field(
        description="__Mandatory__. Allowed values are `consumer` and `business`.",
        alias="categorisationType",
    )
    var_from: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). ",
        alias="from",
    )
    before: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).",
    )
    __properties: ClassVar[List[str]] = [
        "countryCode",
        "categorisationType",
        "from",
        "before",
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
                "countryCode": obj.get("countryCode"),
                "categorisationType": obj.get("categorisationType"),
                "from": obj.get("from"),
                "before": obj.get("before"),
            }
        )
        return _obj
