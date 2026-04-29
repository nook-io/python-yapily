import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class MultiAuthorisation(BaseModel):
    """
    Details the additional levels of authorisation which are required from, and being managed by, the `Institution`.  # noqa: E501
    """

    status: Annotated[
        StrictStr | None,
        Field(description="_Mandatory_. Specifies the current status of the multi-authorisation flow."),
    ] = None
    number_of_authorisation_required: Annotated[
        StrictInt | None,
        Field(
            alias="numberOfAuthorisationRequired", description="__Mandatory__. Total number of authorisations required."
        ),
    ] = None
    number_of_authorisation_received: Annotated[
        StrictInt | None,
        Field(
            alias="numberOfAuthorisationReceived",
            description="__Mandatory__. The total number of authorisations that have been recieved.",
        ),
    ] = None
    last_updated_date_time: Annotated[
        datetime | None,
        Field(
            alias="lastUpdatedDateTime",
            description="__Mandatory__. Date and time of when the authorisation was last updated.",
        ),
    ] = None
    expiration_date_time: Annotated[
        datetime | None,
        Field(
            alias="expirationDateTime",
            description="__Mandatory__. Date and time by when the authorisation flow must be completed before it expires and the authorisation request is terminated.",
        ),
    ] = None
    __properties = [
        "status",
        "numberOfAuthorisationRequired",
        "numberOfAuthorisationReceived",
        "lastUpdatedDateTime",
        "expirationDateTime",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "MultiAuthorisation":
        """Create an instance of MultiAuthorisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "MultiAuthorisation":
        """Create an instance of MultiAuthorisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MultiAuthorisation.model_validate(obj)

        return MultiAuthorisation.model_validate(
            {
                "status": obj.get("status"),
                "number_of_authorisation_required": obj.get("numberOfAuthorisationRequired"),
                "number_of_authorisation_received": obj.get("numberOfAuthorisationReceived"),
                "last_updated_date_time": obj.get("lastUpdatedDateTime"),
                "expiration_date_time": obj.get("expirationDateTime"),
            }
        )
