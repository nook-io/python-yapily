import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr


class PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner(BaseModel):
    """
    PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner
    """

    type: StrictStr | None = None
    code: Annotated[StrictFloat | StrictInt | None, Field(description="A 5 digit error code")] = None
    message: StrictStr | None = None
    __properties = ["type", "code", "message"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner":
        """Create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner":
        """Create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.model_validate(obj)

        return PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.model_validate(
            {"type": obj.get("type"), "code": obj.get("code"), "message": obj.get("message")}
        )
