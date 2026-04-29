import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.register_webhook_request_callback_url_backup import RegisterWebhookRequestCallbackUrlBackup
from yapily.models.register_webhook_request_callback_url_main import RegisterWebhookRequestCallbackUrlMain


class RegisterWebhookRequestCallbackUrl(BaseModel):
    """
    RegisterWebhookRequestCallbackUrl
    """

    main: Annotated[RegisterWebhookRequestCallbackUrlMain, Field()]
    backup: RegisterWebhookRequestCallbackUrlBackup | None = None
    __properties = ["main", "backup"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RegisterWebhookRequestCallbackUrl":
        """Create an instance of RegisterWebhookRequestCallbackUrl from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of main
        if self.main:
            _dict["main"] = self.main.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backup
        if self.backup:
            _dict["backup"] = self.backup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "RegisterWebhookRequestCallbackUrl":
        """Create an instance of RegisterWebhookRequestCallbackUrl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterWebhookRequestCallbackUrl.model_validate(obj)

        return RegisterWebhookRequestCallbackUrl.model_validate(
            {
                "main": RegisterWebhookRequestCallbackUrlMain.from_dict(obj.get("main"))
                if obj.get("main") is not None
                else None,
                "backup": RegisterWebhookRequestCallbackUrlBackup.from_dict(obj.get("backup"))
                if obj.get("backup") is not None
                else None,
            }
        )
