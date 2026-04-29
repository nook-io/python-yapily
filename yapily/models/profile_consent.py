import json
import pprint
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class ProfileConsent(BaseModel):
    """
    Details of a consent linked to a `User Profile`.  # noqa: E501
    """

    id: Annotated[
        StrictStr | None, Field(description="Unique identifier of the `consent` in context of a user's profile.")
    ] = None
    status: Annotated[StrictStr | None, Field(description="The status, can be PENDING, COMPLETED or ERROR.")] = None
    user_id: Annotated[StrictStr | None, Field(alias="userId", description="The userUuid.")] = None
    reference_consent_id: Annotated[
        StrictStr | None, Field(alias="referenceConsentId", description="Unique identifier of the consent.")
    ] = None
    institution_id: Annotated[
        StrictStr | None,
        Field(
            alias="institutionId", description="__Mandatory__. The  `Institution` the authorisation request is sent to."
        ),
    ] = None
    created_at: Annotated[
        datetime | None, Field(alias="createdAt", description="When a profile consent is created.")
    ] = None
    expires_at: Annotated[
        datetime | None, Field(alias="expiresAt", description="When a profile consent is expired after created + X.")
    ] = None
    data_inserted_at: Annotated[
        datetime | None,
        Field(alias="dataInsertedAt", description="After data retrieval from aggregated profile consent is completed."),
    ] = None
    __properties = [
        "id",
        "status",
        "userId",
        "referenceConsentId",
        "institutionId",
        "createdAt",
        "expiresAt",
        "dataInsertedAt",
    ]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ProfileConsent":
        """Create an instance of ProfileConsent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "ProfileConsent":
        """Create an instance of ProfileConsent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfileConsent.model_validate(obj)

        return ProfileConsent.model_validate(
            {
                "id": obj.get("id"),
                "status": obj.get("status"),
                "user_id": obj.get("userId"),
                "reference_consent_id": obj.get("referenceConsentId"),
                "institution_id": obj.get("institutionId"),
                "created_at": obj.get("createdAt"),
                "expires_at": obj.get("expiresAt"),
                "data_inserted_at": obj.get("dataInsertedAt"),
            }
        )
