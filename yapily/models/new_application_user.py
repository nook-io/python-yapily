import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class NewApplicationUser(BaseModel):
    """
    Details of a new user to be created for the application.  # noqa: E501
    """

    application_user_id: Annotated[
        StrictStr | None,
        Field(
            alias="applicationUserId",
            description="__Optional__. The unique identifier of the `Application User` assigned by the Application Owner.",
        ),
    ] = None
    reference_id: Annotated[
        StrictStr | None,
        Field(alias="referenceId", description="__Deprecated__. A non-unique reference Id for the `Application User`."),
    ] = None
    __properties = ["applicationUserId", "referenceId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "NewApplicationUser":
        """Create an instance of NewApplicationUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "NewApplicationUser":
        """Create an instance of NewApplicationUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NewApplicationUser.parse_obj(obj)

        return NewApplicationUser.parse_obj(
            {"application_user_id": obj.get("applicationUserId"), "reference_id": obj.get("referenceId")}
        )
