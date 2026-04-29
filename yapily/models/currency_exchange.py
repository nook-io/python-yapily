import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr


class CurrencyExchange(BaseModel):
    """
    Provides details on the currrency exchange.  # noqa: E501
    """

    source_currency: Annotated[
        StrictStr | None, Field(alias="sourceCurrency", description="Currency from which an amount is to be converted.")
    ] = None
    target_currency: Annotated[
        StrictStr | None, Field(alias="targetCurrency", description="Currency to which an amount is to be converted.")
    ] = None
    unit_currency: Annotated[
        StrictStr | None,
        Field(
            alias="unitCurrency",
            description="The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.",
        ),
    ] = None
    exchange_rate: Annotated[
        StrictFloat | StrictInt | None,
        Field(
            alias="exchangeRate",
            description="The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.",
        ),
    ] = None
    __properties = ["sourceCurrency", "targetCurrency", "unitCurrency", "exchangeRate"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "CurrencyExchange":
        """Create an instance of CurrencyExchange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "CurrencyExchange":
        """Create an instance of CurrencyExchange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrencyExchange.model_validate(obj)

        return CurrencyExchange.model_validate(
            {
                "source_currency": obj.get("sourceCurrency"),
                "target_currency": obj.get("targetCurrency"),
                "unit_currency": obj.get("unitCurrency"),
                "exchange_rate": obj.get("exchangeRate"),
            }
        )
