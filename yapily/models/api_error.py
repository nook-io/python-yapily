import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.institution_error import InstitutionError


class ApiError(BaseModel):
    """
    Provides details of the error that has occurred.  # noqa: E501
    """

    code: Annotated[
        StrictInt | None, Field(description="_Mandatory_. Numeric `HTTP` status code associated with the error.")
    ] = None
    institution_error: Annotated[InstitutionError | None, Field(alias="institutionError")] = None
    message: Annotated[
        StrictStr | None, Field(description="__Mandatory__. Description of the exact error that has been experienced.")
    ] = None
    source: StrictStr | None = None
    status: Annotated[
        StrictStr | None, Field(description="__Mandatory__. Textual description of the `HTTP` error status type.")
    ] = None
    tracing_id: Annotated[
        StrictStr | None,
        Field(
            alias="tracingId",
            description="_Optional_.  A unique identifier assigned by Yapily for the request that can be used for support purposes.",
        ),
    ] = None
    __properties = ["code", "institutionError", "message", "source", "status", "tracingId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiError":
        """Create an instance of ApiError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of institution_error
        if self.institution_error:
            _dict["institutionError"] = self.institution_error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiError":
        """Create an instance of ApiError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiError.model_validate(obj)

        return ApiError.model_validate(
            {
                "code": obj.get("code"),
                "institution_error": InstitutionError.from_dict(obj.get("institutionError"))
                if obj.get("institutionError") is not None
                else None,
                "message": obj.get("message"),
                "source": obj.get("source"),
                "status": obj.get("status"),
                "tracing_id": obj.get("tracingId"),
            }
        )
