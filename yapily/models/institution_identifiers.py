import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class InstitutionIdentifiers(BaseModel):
    """
    Specifies the institution requirements for making the payment. Skips the bank selection screen in payment flow if the `institutionId` and `institutionCountryCode` are provided.  # noqa: E501
    """

    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId",
            description="Yapily identifier which identifies the `Institution` the payment request is sent to.",
        ),
    ] = None
    institution_country_code: Annotated[
        StrictStr,
        Field(
            alias="institutionCountryCode",
            description="2 letter ISO Country code of the `Institution` the payment request is sent to.",
        ),
    ]
    __properties = ["institutionId", "institutionCountryCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "InstitutionIdentifiers":
        """Create an instance of InstitutionIdentifiers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "InstitutionIdentifiers":
        """Create an instance of InstitutionIdentifiers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstitutionIdentifiers.model_validate(obj)

        return InstitutionIdentifiers.model_validate(
            {"institution_id": obj.get("institutionId"), "institution_country_code": obj.get("institutionCountryCode")}
        )
