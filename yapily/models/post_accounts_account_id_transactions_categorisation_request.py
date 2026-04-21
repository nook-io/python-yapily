import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class PostAccountsAccountIdTransactionsCategorisationRequest(BaseModel):
    """
    PostAccountsAccountIdTransactionsCategorisationRequest
    """

    country_code: Annotated[
        StrictStr,
        Field(alias="countryCode", description="_Mandatory_, ISO 3166-1 alpha-2 two-letter country codes e.g. GB"),
    ]
    categorisation_type: Annotated[
        StrictStr,
        Field(alias="categorisationType", description="__Mandatory__. Allowed values are `consumer` and `business`."),
    ]
    var_from: Annotated[
        datetime | None,
        Field(
            alias="from",
            description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). ",
        ),
    ] = None
    before: Annotated[
        datetime | None,
        Field(
            description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
        ),
    ] = None
    __properties = ["countryCode", "categorisationType", "from", "before"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PostAccountsAccountIdTransactionsCategorisationRequest":
        """Create an instance of PostAccountsAccountIdTransactionsCategorisationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "PostAccountsAccountIdTransactionsCategorisationRequest":
        """Create an instance of PostAccountsAccountIdTransactionsCategorisationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisationRequest.parse_obj(obj)

        return PostAccountsAccountIdTransactionsCategorisationRequest.parse_obj(
            {
                "country_code": obj.get("countryCode"),
                "categorisation_type": obj.get("categorisationType"),
                "var_from": obj.get("from"),
                "before": obj.get("before"),
            }
        )
