import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from yapily.models.api_error_response_v2_error_issues_inner import ApiErrorResponseV2ErrorIssuesInner


class ApiErrorResponseV2Error(BaseModel):
    """
    ApiErrorResponseV2Error
    """

    tracing_id: Annotated[
        StrictStr,
        Field(alias="tracingId", description="Unique identifier of the request, used by Yapily for support purposes"),
    ]
    code: Annotated[StrictInt, Field(description="Numeric HTTP status code associated with the error")]
    status: Annotated[StrictStr, Field(description="Textual description of the HTTP status")]
    support_url: Annotated[
        StrictStr | None,
        Field(alias="supportUrl", description="Link to where further information regarding the error can be found"),
    ] = None
    source: Annotated[
        StrictStr | None, Field(description="Source of the error. This may be YAPILY, the INSTITUTION, or the USER")
    ] = None
    issues: Annotated[
        list[ApiErrorResponseV2ErrorIssuesInner], Field(description="List of issues relating to the error")
    ]
    __properties = ["tracingId", "code", "status", "supportUrl", "source", "issues"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiErrorResponseV2Error":
        """Create an instance of ApiErrorResponseV2Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in issues (list)
        _items = []
        if self.issues:
            for _item in self.issues:
                if _item:
                    _items.append(_item.to_dict())
            _dict["issues"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiErrorResponseV2Error":
        """Create an instance of ApiErrorResponseV2Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiErrorResponseV2Error.model_validate(obj)

        return ApiErrorResponseV2Error.model_validate(
            {
                "tracing_id": obj.get("tracingId"),
                "code": obj.get("code"),
                "status": obj.get("status"),
                "support_url": obj.get("supportUrl"),
                "source": obj.get("source"),
                "issues": [ApiErrorResponseV2ErrorIssuesInner.from_dict(_item) for _item in obj.get("issues")]
                if obj.get("issues") is not None
                else None,
            }
        )
