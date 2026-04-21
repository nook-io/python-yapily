import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.type import Type


class ScaMethod(BaseModel):
    """
    __Conditional__. Used to update the authorisation with the sca method of the user's choice for the `Institution` that uses the embedded authorisation flow. If the user has multiple sca methods configured, the `Institution` will allow the user to select from each of these options. <br><br>When the user has multiple sca methods for the `Institution`, this is the second step required in the embedded authorisation flow to authorise the `Consent`.  # noqa: E501
    """

    id: Annotated[StrictStr, Field(description="__Mandatory__. The id of the sca method provided by the `Institution`")]
    type: Type | None = None
    description: Annotated[
        StrictStr | None,
        Field(description="__Optional__. A description of the sca method if provided by the `Institution`"),
    ] = None
    information: Annotated[
        StrictStr | None,
        Field(
            description="Additional information from the institution to provide to the PSU to help with the selected SCA method. The language is determined by the institution and may vary."
        ),
    ] = None
    data: Annotated[
        list[StrictStr] | None,
        Field(
            description="Data from the institution to provide to the PSU to complete authorisation. The language is determined by the institution and may vary."
        ),
    ] = None
    __properties = ["id", "type", "description", "information", "data"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ScaMethod":
        """Create an instance of ScaMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ScaMethod":
        """Create an instance of ScaMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScaMethod.parse_obj(obj)

        return ScaMethod.parse_obj(
            {
                "id": obj.get("id"),
                "type": obj.get("type"),
                "description": obj.get("description"),
                "information": obj.get("information"),
                "data": obj.get("data"),
            }
        )
