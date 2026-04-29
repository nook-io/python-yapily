import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class UserCredentials(BaseModel):
    """
    __Conditional__. Used to capture the user's credentials to allow them to login to an `Institution` that uses the embedded account authorisation flow. <br><br>This is the first step required in the embedded account authorisation flow to authorise the `Consent`.  # noqa: E501
    """

    id: Annotated[
        StrictStr, Field(description="__Mandatory__. The login id for the user for a particular `Institution`.")
    ]
    corporate_id: Annotated[
        StrictStr | None,
        Field(
            alias="corporateId",
            description="__Conditional__. The corporate login for the user for a particular corporate `Institution`.",
        ),
    ] = None
    password: Annotated[
        StrictStr, Field(description="__Mandatory__. The password of the user to login to a particular `Institution`.")
    ]
    __properties = ["id", "corporateId", "password"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "UserCredentials":
        """Create an instance of UserCredentials from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "UserCredentials":
        """Create an instance of UserCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserCredentials.model_validate(obj)

        return UserCredentials.model_validate(
            {"id": obj.get("id"), "corporate_id": obj.get("corporateId"), "password": obj.get("password")}
        )
