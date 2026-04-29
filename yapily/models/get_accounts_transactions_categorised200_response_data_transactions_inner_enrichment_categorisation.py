import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation(BaseModel):
    """
    GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation
    """

    categories: Annotated[list[StrictStr], Field()] | None = None
    __properties = ["categories"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> "GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation":
        """Create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation.model_validate(
                obj
            )

        return GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation.model_validate(
            {"categories": obj.get("categories")}
        )
