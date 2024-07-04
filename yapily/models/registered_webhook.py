# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from yapily.models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl

class RegisteredWebhook(BaseModel):
    """
    RegisteredWebhook
    """
    id: Optional[StrictStr] = Field(None, description="the UUID of the registered webhook, used to update or remove the webhook")
    application_id: Optional[StrictStr] = Field(None, alias="applicationId", description="user applicaiton id")
    categories: Optional[conlist(StrictStr)] = None
    callback_url: Optional[RegisteredWebhookCallbackUrl] = Field(None, alias="callbackUrl")
    metadata: Optional[Dict[str, StrictStr]] = None
    __properties = ["id", "applicationId", "categories", "callbackUrl", "metadata"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RegisteredWebhook:
        """Create an instance of RegisteredWebhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of callback_url
        if self.callback_url:
            _dict['callbackUrl'] = self.callback_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegisteredWebhook:
        """Create an instance of RegisteredWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisteredWebhook.parse_obj(obj)

        _obj = RegisteredWebhook.parse_obj({
            "id": obj.get("id"),
            "application_id": obj.get("applicationId"),
            "categories": obj.get("categories"),
            "callback_url": RegisteredWebhookCallbackUrl.from_dict(obj.get("callbackUrl")) if obj.get("callbackUrl") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


