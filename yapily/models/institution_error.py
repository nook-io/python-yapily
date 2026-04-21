import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class InstitutionError(BaseModel):
    """
    Raw error details provided by the `Institution`, when it was the error source.  # noqa: E501
    """

    error_message: Annotated[
        StrictStr | None, Field(alias="errorMessage", description="Textual description of the `Institution` error.")
    ] = None
    http_status_code: Annotated[
        StrictInt | None,
        Field(alias="httpStatusCode", description="Numeric HTTP status code associated with the `Institution` error."),
    ] = None
    __properties = ["errorMessage", "httpStatusCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "InstitutionError":
        """Create an instance of InstitutionError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "InstitutionError":
        """Create an instance of InstitutionError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstitutionError.parse_obj(obj)

        return InstitutionError.parse_obj(
            {"error_message": obj.get("errorMessage"), "http_status_code": obj.get("httpStatusCode")}
        )
