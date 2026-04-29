import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class InstitutionIdentifiersResponse(BaseModel):
    """
    Specifies the institution selected for making the payment.  # noqa: E501
    """

    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId",
            description="Yapily identifier which identifies the `Institution` the payment request is sent to.",
        ),
    ] = None
    institution_country_code: Annotated[
        StrictStr | None,
        Field(
            alias="institutionCountryCode",
            description="2 letter ISO Country code of the `Institution` the payment request is sent to.",
        ),
    ] = None
    __properties = ["institutionId", "institutionCountryCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "InstitutionIdentifiersResponse":
        """Create an instance of InstitutionIdentifiersResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "InstitutionIdentifiersResponse":
        """Create an instance of InstitutionIdentifiersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstitutionIdentifiersResponse.model_validate(obj)

        return InstitutionIdentifiersResponse.model_validate(
            {"institution_id": obj.get("institutionId"), "institution_country_code": obj.get("institutionCountryCode")}
        )
