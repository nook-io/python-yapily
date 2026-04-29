import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr

from yapily.models.rate_type_enum import RateTypeEnum


class ExchangeRateInformationResponse(BaseModel):
    """
    ExchangeRateInformationResponse
    """

    unit_currency: Annotated[
        StrictStr,
        Field(
            alias="unitCurrency",
            description="__Mandatory__. The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is `GBP`.",
        ),
    ]
    rate: Annotated[
        StrictFloat | StrictInt | None,
        Field(
            description="__Optional__. The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency."
        ),
    ] = None
    rate_type: Annotated[RateTypeEnum, Field(alias="rateType")]
    foreign_exchange_contract_reference: Annotated[
        StrictStr | None,
        Field(
            alias="foreignExchangeContractReference",
            description="__Optional__. The unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.",
        ),
    ] = None
    exchange_rate_expiry_date: Annotated[datetime | None, Field(alias="exchangeRateExpiryDate")] = None
    __properties = ["unitCurrency", "rate", "rateType", "foreignExchangeContractReference", "exchangeRateExpiryDate"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ExchangeRateInformationResponse":
        """Create an instance of ExchangeRateInformationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ExchangeRateInformationResponse":
        """Create an instance of ExchangeRateInformationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExchangeRateInformationResponse.model_validate(obj)

        return ExchangeRateInformationResponse.model_validate(
            {
                "unit_currency": obj.get("unitCurrency"),
                "rate": obj.get("rate"),
                "rate_type": obj.get("rateType"),
                "foreign_exchange_contract_reference": obj.get("foreignExchangeContractReference"),
                "exchange_rate_expiry_date": obj.get("exchangeRateExpiryDate"),
            }
        )
