import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class GetBulkPaymentStatus200ResponseDataStatusDetails(BaseModel):
    """
    GetBulkPaymentStatus200ResponseDataStatusDetails
    """

    status: Annotated[
        StrictStr | None, Field(description="Bulk file status. Enum: `COMPLETED` `PENDING` `FAILED` `UNKNOWN`")
    ] = None
    updated_at: Annotated[StrictStr | None, Field(alias="updatedAt")] = None
    __properties = ["status", "updatedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "GetBulkPaymentStatus200ResponseDataStatusDetails":
        """Create an instance of GetBulkPaymentStatus200ResponseDataStatusDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "GetBulkPaymentStatus200ResponseDataStatusDetails":
        """Create an instance of GetBulkPaymentStatus200ResponseDataStatusDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetBulkPaymentStatus200ResponseDataStatusDetails.parse_obj(obj)

        return GetBulkPaymentStatus200ResponseDataStatusDetails.parse_obj(
            {"status": obj.get("status"), "updated_at": obj.get("updatedAt")}
        )
