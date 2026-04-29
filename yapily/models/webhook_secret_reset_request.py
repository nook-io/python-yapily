import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class WebhookSecretResetRequest(BaseModel):
    """
    WebhookSecretResetRequest
    """

    delay: Annotated[
        Annotated[float, Field(le=86400, ge=0, strict=True)] | Annotated[int, Field(le=86400, ge=0, strict=True)],
        Field(description="delay in seconds"),
    ]
    __properties = ["delay"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "WebhookSecretResetRequest":
        """Create an instance of WebhookSecretResetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "WebhookSecretResetRequest":
        """Create an instance of WebhookSecretResetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookSecretResetRequest.model_validate(obj)

        return WebhookSecretResetRequest.model_validate({"delay": obj.get("delay")})
