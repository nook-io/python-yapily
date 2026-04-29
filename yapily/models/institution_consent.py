import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class InstitutionConsent(BaseModel):
    """
    `Institution` authorised consents which are currently in place for the `Application User`.  # noqa: E501
    """

    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId", description="__Mandatory__. The `Institution` the authorisation request is sent to."
        ),
    ] = None
    __properties = ["institutionId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "InstitutionConsent":
        """Create an instance of InstitutionConsent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "InstitutionConsent":
        """Create an instance of InstitutionConsent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstitutionConsent.model_validate(obj)

        return InstitutionConsent.model_validate({"institution_id": obj.get("institutionId")})
