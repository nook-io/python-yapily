# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from yapily.models.error_details import ErrorDetails
from yapily.models.monitoring_endpoint_status import MonitoringEndpointStatus

class Model401VirtualAccountsApiErrorResponse(BaseModel):
    """
    Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/#yapily-api-financial-data) and any [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the `Consent` is no longer authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create User](https://docs.yapily.com/api/#create-user)</li><li>`424` - Returned by any [Financial Data](https://docs.yapily.com/api/#yapily-api-financial-data) and any [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the feature to be accessed is not supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any false positives, please <a href=\"mailto:support@yapily.com\">notify us</a></li></ul>  # noqa: E501
    """
    error: Optional[ErrorDetails] = None
    monitoring: Optional[conlist(MonitoringEndpointStatus)] = None
    __properties = ["error", "monitoring"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Model401VirtualAccountsApiErrorResponse:
        """Create an instance of Model401VirtualAccountsApiErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in monitoring (list)
        _items = []
        if self.monitoring:
            for _item in self.monitoring:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monitoring'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model401VirtualAccountsApiErrorResponse:
        """Create an instance of Model401VirtualAccountsApiErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Model401VirtualAccountsApiErrorResponse.parse_obj(obj)

        _obj = Model401VirtualAccountsApiErrorResponse.parse_obj({
            "error": ErrorDetails.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "monitoring": [MonitoringEndpointStatus.from_dict(_item) for _item in obj.get("monitoring")] if obj.get("monitoring") is not None else None
        })
        return _obj


