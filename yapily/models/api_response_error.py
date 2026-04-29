import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from yapily.models.api_error import ApiError
from yapily.models.raw_response import RawResponse


class ApiResponseError(BaseModel):
    """
    Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the `Consent` is no longer authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create User](https://docs.yapily.com/api/reference/#operation/addUser)</li><li>`424` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the feature to be accessed is not supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any false positives, please <a href=\"mailto:support@yapily.com\">notify us</a></li></ul>  # noqa: E501
    """

    error: ApiError | None = None
    raw: Annotated[list[RawResponse], Field()] | None = None
    __properties = ["error", "raw"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "ApiResponseError":
        """Create an instance of ApiResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item in self.raw:
                if _item:
                    _items.append(_item.to_dict())
            _dict["raw"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "ApiResponseError":
        """Create an instance of ApiResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResponseError.model_validate(obj)

        return ApiResponseError.model_validate(
            {
                "error": ApiError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
                "raw": [RawResponse.from_dict(_item) for _item in obj.get("raw")]
                if obj.get("raw") is not None
                else None,
            }
        )
