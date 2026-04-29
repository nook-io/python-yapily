import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class RegisterWebhookRequestCallbackUrlBackup(BaseModel):
    """
    backup webhook url used to send events to in case the main one is not responding  # noqa: E501
    """

    url: StrictStr | None = None
    __properties = ["url"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "RegisterWebhookRequestCallbackUrlBackup":
        """Create an instance of RegisterWebhookRequestCallbackUrlBackup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "RegisterWebhookRequestCallbackUrlBackup":
        """Create an instance of RegisterWebhookRequestCallbackUrlBackup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterWebhookRequestCallbackUrlBackup.model_validate(obj)

        return RegisterWebhookRequestCallbackUrlBackup.model_validate({"url": obj.get("url")})
