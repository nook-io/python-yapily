from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl
from yapily.models.webhook_status_type import WebhookStatusType
from typing import Set
from typing_extensions import Self


class RegisteredWebhookWithStatus(BaseModel):
    id: Optional[StrictStr] = Field(
        default=None,
        description="the UUID of the registered webhook, used to update or remove the webhook",
    )
    application_id: Optional[StrictStr] = Field(
        default=None, description="user applicaiton id", alias="applicationId"
    )
    categories: Optional[List[StrictStr]] = None
    callback_url: Optional[RegisteredWebhookCallbackUrl] = Field(
        default=None, alias="callbackUrl"
    )
    metadata: Optional[Dict[str, StrictStr]] = None
    status: Optional[WebhookStatusType] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "applicationId",
        "categories",
        "callbackUrl",
        "metadata",
        "status",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.callback_url:
            _dict["callbackUrl"] = self.callback_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "applicationId": obj.get("applicationId"),
                "categories": obj.get("categories"),
                "callbackUrl": RegisteredWebhookCallbackUrl.from_dict(
                    obj["callbackUrl"]
                )
                if obj.get("callbackUrl") is not None
                else None,
                "metadata": obj.get("metadata"),
                "status": obj.get("status"),
            }
        )
        return _obj
