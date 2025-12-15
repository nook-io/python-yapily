from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self


class EnrichedTransaction(BaseModel):
    transaction_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the transaction",
        alias="transactionId",
    )
    transaction_information: Optional[StrictStr] = Field(
        default=None,
        description="Information for the transaction",
        alias="transactionInformation",
    )
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Monetary amount."
    )
    institution: Optional[StrictStr] = Field(
        default=None, description="The `Institution` that the transaction is sent to."
    )
    booking_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time of when a transaction entry occured and was posted to the account servicer's books.",
        alias="bookingDateTime",
    )
    __properties: ClassVar[List[str]] = [
        "transactionId",
        "transactionInformation",
        "amount",
        "institution",
        "bookingDateTime",
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
                "transactionId": obj.get("transactionId"),
                "transactionInformation": obj.get("transactionInformation"),
                "amount": obj.get("amount"),
                "institution": obj.get("institution"),
                "bookingDateTime": obj.get("bookingDateTime"),
            }
        )
        return _obj
