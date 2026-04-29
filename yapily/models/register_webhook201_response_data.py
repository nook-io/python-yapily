import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl
from yapily.models.webhook_status_type import WebhookStatusType


class RegisterWebhook201ResponseData(BaseModel):
    """
    RegisterWebhook201ResponseData
    """

    id: Annotated[
        StrictStr | None, Field(description="the UUID of the registered webhook, used to update or remove the webhook")
    ] = None
    application_id: Annotated[StrictStr | None, Field(alias="applicationId", description="user applicaiton id")] = None
    categories: Annotated[list[StrictStr], Field()] | None = None
    callback_url: Annotated[RegisteredWebhookCallbackUrl | None, Field(alias="callbackUrl")] = None
    metadata: dict[str, StrictStr] | None = None
    status: WebhookStatusType | None = None
    webhook_secret: Annotated[
        StrictStr | None,
        Field(alias="webhookSecret", description="HMAC secret needed to validate that the request payload is genuine"),
    ] = None
    __properties = ["id", "applicationId", "categories", "callbackUrl", "metadata", "status", "webhookSecret"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RegisterWebhook201ResponseData":
        """Create an instance of RegisterWebhook201ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of callback_url
        if self.callback_url:
            _dict["callbackUrl"] = self.callback_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RegisterWebhook201ResponseData":
        """Create an instance of RegisterWebhook201ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterWebhook201ResponseData.model_validate(obj)

        return RegisterWebhook201ResponseData.model_validate(
            {
                "id": obj.get("id"),
                "application_id": obj.get("applicationId"),
                "categories": obj.get("categories"),
                "callback_url": RegisteredWebhookCallbackUrl.from_dict(obj.get("callbackUrl"))
                if obj.get("callbackUrl") is not None
                else None,
                "metadata": obj.get("metadata"),
                "status": obj.get("status"),
                "webhook_secret": obj.get("webhookSecret"),
            }
        )
