import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.request_constraints import RequestConstraints


class DataConstraintsResponse(BaseModel):
    """
    DataConstraintsResponse
    """

    institution_id: Annotated[
        StrictStr, Field(alias="institutionId", description="The id to represent the `Institution`.")
    ]
    institution_country_code: Annotated[
        StrictStr | None,
        Field(alias="institutionCountryCode", description="2 letter ISO Country code of the `Institution`."),
    ] = None
    endpoint_path: Annotated[
        StrictStr | None, Field(alias="endpointPath", description="Define the applicable API end point.")
    ] = None
    endpoint_method: Annotated[
        StrictStr | None, Field(alias="endpointMethod", description="Https Method for the endpoint.")
    ] = None
    request: Annotated[RequestConstraints, Field()]
    __properties = ["institutionId", "institutionCountryCode", "endpointPath", "endpointMethod", "request"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "DataConstraintsResponse":
        """Create an instance of DataConstraintsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of request
        if self.request:
            _dict["request"] = self.request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "DataConstraintsResponse":
        """Create an instance of DataConstraintsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataConstraintsResponse.parse_obj(obj)

        return DataConstraintsResponse.parse_obj(
            {
                "institution_id": obj.get("institutionId"),
                "institution_country_code": obj.get("institutionCountryCode"),
                "endpoint_path": obj.get("endpointPath"),
                "endpoint_method": obj.get("endpointMethod"),
                "request": RequestConstraints.from_dict(obj.get("request")) if obj.get("request") is not None else None,
            }
        )
