import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.account_identification import AccountIdentification


class AccountInfo(BaseModel):
    """
    __Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.  # noqa: E501
    """

    account_id: Annotated[
        StrictStr | None, Field(alias="accountId", description="__Conditional__. Unique identifier of the account.")
    ] = None
    account_identification: Annotated[AccountIdentification, Field(alias="accountIdentification")]
    __properties = ["accountId", "accountIdentification"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "AccountInfo":
        """Create an instance of AccountInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account_identification
        if self.account_identification:
            _dict["accountIdentification"] = self.account_identification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "AccountInfo":
        """Create an instance of AccountInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountInfo.parse_obj(obj)

        return AccountInfo.parse_obj(
            {
                "account_id": obj.get("accountId"),
                "account_identification": AccountIdentification.from_dict(obj.get("accountIdentification"))
                if obj.get("accountIdentification") is not None
                else None,
            }
        )
