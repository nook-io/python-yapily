from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class MultiAuthorisation(BaseModel):
    status: Optional[StrictStr] = Field(
        default=None,
        description="_Mandatory_. Specifies the current status of the multi-authorisation flow.",
    )
    number_of_authorisation_required: Optional[StrictInt] = Field(
        default=None,
        description="__Mandatory__. Total number of authorisations required.",
        alias="numberOfAuthorisationRequired",
    )
    number_of_authorisation_received: Optional[StrictInt] = Field(
        default=None,
        description="__Mandatory__. The total number of authorisations that have been recieved.",
        alias="numberOfAuthorisationReceived",
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None,
        description="__Mandatory__. Date and time of when the authorisation was last updated.",
        alias="lastUpdatedDateTime",
    )
    expiration_date_time: Optional[datetime] = Field(
        default=None,
        description="__Mandatory__. Date and time by when the authorisation flow must be completed before it expires and the authorisation request is terminated.",
        alias="expirationDateTime",
    )
    __properties: ClassVar[List[str]] = [
        "status",
        "numberOfAuthorisationRequired",
        "numberOfAuthorisationReceived",
        "lastUpdatedDateTime",
        "expirationDateTime",
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
                "status": obj.get("status"),
                "numberOfAuthorisationRequired": obj.get(
                    "numberOfAuthorisationRequired"
                ),
                "numberOfAuthorisationReceived": obj.get(
                    "numberOfAuthorisationReceived"
                ),
                "lastUpdatedDateTime": obj.get("lastUpdatedDateTime"),
                "expirationDateTime": obj.get("expirationDateTime"),
            }
        )
        return _obj
