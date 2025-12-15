from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.register_webhook_request_callback_url import (
    RegisterWebhookRequestCallbackUrl,
)
from typing import Set
from typing_extensions import Self


class RegisterWebhookRequest(BaseModel):
    application_id: StrictStr = Field(
        description="user application id", alias="applicationId"
    )
    categories: List[StrictStr]
    callback_url: RegisterWebhookRequestCallbackUrl = Field(alias="callbackUrl")
    metadata: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "applicationId",
        "categories",
        "callbackUrl",
        "metadata",
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
                "applicationId": obj.get("applicationId"),
                "categories": obj.get("categories"),
                "callbackUrl": RegisterWebhookRequestCallbackUrl.from_dict(
                    obj["callbackUrl"]
                )
                if obj.get("callbackUrl") is not None
                else None,
                "metadata": obj.get("metadata"),
            }
        )
        return _obj
