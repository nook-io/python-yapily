from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.categorisation import Categorisation
from yapily.models.enrichment_merchant import EnrichmentMerchant
from yapily.models.transaction_hash import TransactionHash
from typing import Set
from typing_extensions import Self


class Enrichment(BaseModel):
    categorisation: Optional[Categorisation] = None
    transaction_hash: Optional[TransactionHash] = Field(
        default=None, alias="transactionHash"
    )
    cleansed_description: Optional[StrictStr] = Field(
        default=None,
        description="Cleaned version of the `Transaction Description` that removes miscellaneous, generic and unhelpful text.",
        alias="cleansedDescription",
    )
    merchant: Optional[EnrichmentMerchant] = None
    location: Optional[StrictStr] = Field(
        default=None, description="The location of where the transaction took place."
    )
    payment_processor: Optional[StrictStr] = Field(
        default=None,
        description="A payment provider that manages (credit/debit) transactions between the `Institution` and the merchant.",
        alias="paymentProcessor",
    )
    corrected_date: Optional[datetime] = Field(
        default=None,
        description="The likely date and time on which the transaction took place. This is distinct from `Booking Date Time` which usually refers to the post-clearing value.",
        alias="correctedDate",
    )
    __properties: ClassVar[List[str]] = [
        "categorisation",
        "transactionHash",
        "cleansedDescription",
        "merchant",
        "location",
        "paymentProcessor",
        "correctedDate",
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
        if self.categorisation:
            _dict["categorisation"] = self.categorisation.to_dict()
        if self.transaction_hash:
            _dict["transactionHash"] = self.transaction_hash.to_dict()
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "categorisation": Categorisation.from_dict(obj["categorisation"])
                if obj.get("categorisation") is not None
                else None,
                "transactionHash": TransactionHash.from_dict(obj["transactionHash"])
                if obj.get("transactionHash") is not None
                else None,
                "cleansedDescription": obj.get("cleansedDescription"),
                "merchant": EnrichmentMerchant.from_dict(obj["merchant"])
                if obj.get("merchant") is not None
                else None,
                "location": obj.get("location"),
                "paymentProcessor": obj.get("paymentProcessor"),
                "correctedDate": obj.get("correctedDate"),
            }
        )
        return _obj
