import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.feature_enum import FeatureEnum


class FeatureDetails(BaseModel):
    """
    Features that an individual `Institution` may support.   # noqa: E501
    """

    feature: FeatureEnum | None = None
    endpoint: Annotated[
        StrictStr | None,
        Field(
            description="Endpoints that are associated with the feature e.g. (available for use if an Institution supports a feature)."
        ),
    ] = None
    documentation_url: Annotated[
        StrictStr | None,
        Field(alias="documentationUrl", description="The link to further documentation regarding the feature."),
    ] = None
    __properties = ["feature", "endpoint", "documentationUrl"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "FeatureDetails":
        """Create an instance of FeatureDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "FeatureDetails":
        """Create an instance of FeatureDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeatureDetails.model_validate(obj)

        return FeatureDetails.model_validate(
            {
                "feature": obj.get("feature"),
                "endpoint": obj.get("endpoint"),
                "documentation_url": obj.get("documentationUrl"),
            }
        )
