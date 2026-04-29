import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class RegisteredWebhookCallbackUrlMain(BaseModel):
    """
    primary webhook url used to send events to  # noqa: E501
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
    def from_json(cls, json_str: str) -> "RegisteredWebhookCallbackUrlMain":
        """Create an instance of RegisteredWebhookCallbackUrlMain from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "RegisteredWebhookCallbackUrlMain":
        """Create an instance of RegisteredWebhookCallbackUrlMain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisteredWebhookCallbackUrlMain.model_validate(obj)

        return RegisteredWebhookCallbackUrlMain.model_validate({"url": obj.get("url")})
