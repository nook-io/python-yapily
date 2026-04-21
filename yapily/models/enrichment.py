import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.categorisation import Categorisation
from yapily.models.enrichment_merchant import EnrichmentMerchant
from yapily.models.transaction_hash import TransactionHash


class Enrichment(BaseModel):
    """
    Enriched data that has been derived by Yapily using it's data processing and machine learning techniques.  # noqa: E501
    """

    categorisation: Categorisation | None = None
    transaction_hash: Annotated[TransactionHash | None, Field(alias="transactionHash")] = None
    cleansed_description: Annotated[
        StrictStr | None,
        Field(
            alias="cleansedDescription",
            description="Cleaned version of the `Transaction Description` that removes miscellaneous, generic and unhelpful text.",
        ),
    ] = None
    merchant: EnrichmentMerchant | None = None
    location: Annotated[StrictStr | None, Field(description="The location of where the transaction took place.")] = None
    payment_processor: Annotated[
        StrictStr | None,
        Field(
            alias="paymentProcessor",
            description="A payment provider that manages (credit/debit) transactions between the `Institution` and the merchant.",
        ),
    ] = None
    corrected_date: Annotated[
        datetime | None,
        Field(
            alias="correctedDate",
            description="The likely date and time on which the transaction took place. This is distinct from `Booking Date Time` which usually refers to the post-clearing value.",
        ),
    ] = None
    __properties = [
        "categorisation",
        "transactionHash",
        "cleansedDescription",
        "merchant",
        "location",
        "paymentProcessor",
        "correctedDate",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Enrichment":
        """Create an instance of Enrichment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of categorisation
        if self.categorisation:
            _dict["categorisation"] = self.categorisation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction_hash
        if self.transaction_hash:
            _dict["transactionHash"] = self.transaction_hash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict["merchant"] = self.merchant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "Enrichment":
        """Create an instance of Enrichment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Enrichment.parse_obj(obj)

        return Enrichment.parse_obj(
            {
                "categorisation": Categorisation.from_dict(obj.get("categorisation"))
                if obj.get("categorisation") is not None
                else None,
                "transaction_hash": TransactionHash.from_dict(obj.get("transactionHash"))
                if obj.get("transactionHash") is not None
                else None,
                "cleansed_description": obj.get("cleansedDescription"),
                "merchant": EnrichmentMerchant.from_dict(obj.get("merchant"))
                if obj.get("merchant") is not None
                else None,
                "location": obj.get("location"),
                "payment_processor": obj.get("paymentProcessor"),
                "corrected_date": obj.get("correctedDate"),
            }
        )
