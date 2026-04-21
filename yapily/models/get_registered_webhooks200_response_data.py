import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.registered_webhook_with_status import RegisteredWebhookWithStatus


class GetRegisteredWebhooks200ResponseData(BaseModel):
    """
    GetRegisteredWebhooks200ResponseData
    """

    active: Annotated[list[RegisteredWebhookWithStatus], Field()] | None = None
    __properties = ["active"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetRegisteredWebhooks200ResponseData":
        """Create an instance of GetRegisteredWebhooks200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in active (list)
        _items = []
        if self.active:
            for _item in self.active:
                if _item:
                    _items.append(_item.to_dict())
            _dict["active"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "GetRegisteredWebhooks200ResponseData":
        """Create an instance of GetRegisteredWebhooks200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRegisteredWebhooks200ResponseData.parse_obj(obj)

        return GetRegisteredWebhooks200ResponseData.parse_obj(
            {
                "active": [RegisteredWebhookWithStatus.from_dict(_item) for _item in obj.get("active")]
                if obj.get("active") is not None
                else None
            }
        )
