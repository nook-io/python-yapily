import json
import pprint

from pydantic import BaseModel, ConfigDict

from yapily.models.metadata import Metadata
from yapily.models.register_webhook201_response_data import RegisterWebhook201ResponseData


class WebhookDetailsWithSecret(BaseModel):
    """
    WebhookDetailsWithSecret
    """

    metadata: Metadata | None = None
    data: RegisterWebhook201ResponseData | None = None
    __properties = ["metadata", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "WebhookDetailsWithSecret":
        """Create an instance of WebhookDetailsWithSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "WebhookDetailsWithSecret":
        """Create an instance of WebhookDetailsWithSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookDetailsWithSecret.model_validate(obj)

        return WebhookDetailsWithSecret.model_validate(
            {
                "metadata": Metadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
                "data": RegisterWebhook201ResponseData.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
            }
        )
