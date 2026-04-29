import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr


class EnrichedTransaction(BaseModel):
    """
    Details of the transaction, identified by Yapily data services.  # noqa: E501
    """

    transaction_id: Annotated[
        StrictStr | None, Field(alias="transactionId", description="Unique identifier of the transaction")
    ] = None
    transaction_information: Annotated[
        StrictStr | None, Field(alias="transactionInformation", description="Information for the transaction")
    ] = None
    amount: Annotated[StrictFloat | StrictInt | None, Field(description="Monetary amount.")] = None
    institution: Annotated[
        StrictStr | None, Field(description="The `Institution` that the transaction is sent to.")
    ] = None
    booking_date_time: Annotated[
        datetime | None,
        Field(
            alias="bookingDateTime",
            description="Date and time of when a transaction entry occured and was posted to the account servicer's books.",
        ),
    ] = None
    __properties = ["transactionId", "transactionInformation", "amount", "institution", "bookingDateTime"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EnrichedTransaction":
        """Create an instance of EnrichedTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "EnrichedTransaction":
        """Create an instance of EnrichedTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichedTransaction.model_validate(obj)

        return EnrichedTransaction.model_validate(
            {
                "transaction_id": obj.get("transactionId"),
                "transaction_information": obj.get("transactionInformation"),
                "amount": obj.get("amount"),
                "institution": obj.get("institution"),
                "booking_date_time": obj.get("bookingDateTime"),
            }
        )
