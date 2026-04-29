import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.register_webhook_request_callback_url import RegisterWebhookRequestCallbackUrl


class RegisterWebhookRequest(BaseModel):
    """
    RegisterWebhookRequest
    """

    application_id: Annotated[StrictStr, Field(alias="applicationId", description="user application id")]
    categories: Annotated[list[StrictStr], Field()]
    callback_url: Annotated[RegisterWebhookRequestCallbackUrl, Field(alias="callbackUrl")]
    metadata: dict[str, StrictStr] | None = None
    __properties = ["applicationId", "categories", "callbackUrl", "metadata"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RegisterWebhookRequest":
        """Create an instance of RegisterWebhookRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of callback_url
        if self.callback_url:
            _dict["callbackUrl"] = self.callback_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RegisterWebhookRequest":
        """Create an instance of RegisterWebhookRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterWebhookRequest.model_validate(obj)

        return RegisterWebhookRequest.model_validate(
            {
                "application_id": obj.get("applicationId"),
                "categories": obj.get("categories"),
                "callback_url": RegisterWebhookRequestCallbackUrl.from_dict(obj.get("callbackUrl"))
                if obj.get("callbackUrl") is not None
                else None,
                "metadata": obj.get("metadata"),
            }
        )
