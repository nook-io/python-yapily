import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class SearchApplicationsPublicFilterValuesParameter(BaseModel):
    """
    SearchApplicationsPublicFilterValuesParameter
    """

    application_ids: Annotated[
        Annotated[list[StrictStr], Field(max_length=15)] | None,
        Field(
            alias="applicationIds",
            description="Sub-application ids to filter the results for. If provided, the results will only include sub-applications with the given ids. Non-existent ids will be ignored.",
        ),
    ] = None
    offset: Annotated[
        Annotated[int, Field(strict=True, ge=0)] | None, Field(description="The number of results to skip.")
    ] = 0
    limit: Annotated[
        Annotated[int, Field(strict=True, le=1000, ge=1)] | None,
        Field(description="The maximum number of results to return."),
    ] = 1000
    sort: Annotated[
        StrictStr | None,
        Field(
            description="The field to sort the results by.<br><br>Possible values:<ul><li>`last_updated` (ascending)</li><li>`-last_updated` (descending)</li><li>`name` (ascending)</li><li>`-name` (descending)</li><li>`uuid` (ascending)</li><li>`-uuid` (descending)</li></ul>"
        ),
    ] = "name"
    __properties = ["applicationIds", "offset", "limit", "sort"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "SearchApplicationsPublicFilterValuesParameter":
        """Create an instance of SearchApplicationsPublicFilterValuesParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "SearchApplicationsPublicFilterValuesParameter":
        """Create an instance of SearchApplicationsPublicFilterValuesParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchApplicationsPublicFilterValuesParameter.model_validate(obj)

        return SearchApplicationsPublicFilterValuesParameter.model_validate(
            {
                "application_ids": obj.get("applicationIds"),
                "offset": obj.get("offset") if obj.get("offset") is not None else 0,
                "limit": obj.get("limit") if obj.get("limit") is not None else 1000,
                "sort": obj.get("sort") if obj.get("sort") is not None else "name",
            }
        )
