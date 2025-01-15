# coding: utf-8

"""
Yapily API

The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

The version of the OpenAPI document: 7.2.0
Contact: support@yapily.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.api_error import ApiError
from yapily.models.raw_response import RawResponse
from typing import Set
from typing_extensions import Self


class ApiResponseError(BaseModel):
    """
    Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the `Consent` is no longer authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create User](https://docs.yapily.com/api/reference/#operation/addUser)</li><li>`424` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the feature to be accessed is not supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any false positives, please <a href=\"mailto:support@yapily.com\">notify us</a></li></ul>
    """  # noqa: E501

    error: Optional[ApiError] = None
    raw: Optional[List[RawResponse]] = None
    __properties: ClassVar[List[str]] = ["error", "raw"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in raw (list)
        _items = []
        if self.raw:
            for _item_raw in self.raw:
                if _item_raw:
                    _items.append(_item_raw.to_dict())
            _dict["raw"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "error": ApiError.from_dict(obj["error"])
                if obj.get("error") is not None
                else None,
                "raw": [RawResponse.from_dict(_item) for _item in obj["raw"]]
                if obj.get("raw") is not None
                else None,
            }
        )
        return _obj
