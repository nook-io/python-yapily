from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.register_webhook_request_callback_url_backup import (
    RegisterWebhookRequestCallbackUrlBackup,
)
from yapily.models.register_webhook_request_callback_url_main import (
    RegisterWebhookRequestCallbackUrlMain,
)
from typing import Set
from typing_extensions import Self


class RegisterWebhookRequestCallbackUrl(BaseModel):
    main: RegisterWebhookRequestCallbackUrlMain
    backup: Optional[RegisterWebhookRequestCallbackUrlBackup] = None
    __properties: ClassVar[List[str]] = ["main", "backup"]
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
        if self.main:
            _dict["main"] = self.main.to_dict()
        if self.backup:
            _dict["backup"] = self.backup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "main": RegisterWebhookRequestCallbackUrlMain.from_dict(obj["main"])
                if obj.get("main") is not None
                else None,
                "backup": RegisterWebhookRequestCallbackUrlBackup.from_dict(
                    obj["backup"]
                )
                if obj.get("backup") is not None
                else None,
            }
        )
        return _obj
