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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MultiAuthorisation(BaseModel):
    """
    Details the additional levels of authorisation which are required from, and being managed by, the `Institution`.
    """ # noqa: E501
    status: Optional[StrictStr] = Field(default=None, description="_Mandatory_. Specifies the current status of the multi-authorisation flow.")
    number_of_authorisation_required: Optional[StrictInt] = Field(default=None, description="__Mandatory__. Total number of authorisations required.", alias="numberOfAuthorisationRequired")
    number_of_authorisation_received: Optional[StrictInt] = Field(default=None, description="__Mandatory__. The total number of authorisations that have been recieved.", alias="numberOfAuthorisationReceived")
    last_updated_date_time: Optional[datetime] = Field(default=None, description="__Mandatory__. Date and time of when the authorisation was last updated.", alias="lastUpdatedDateTime")
    expiration_date_time: Optional[datetime] = Field(default=None, description="__Mandatory__. Date and time by when the authorisation flow must be completed before it expires and the authorisation request is terminated.", alias="expirationDateTime")
    __properties: ClassVar[List[str]] = ["status", "numberOfAuthorisationRequired", "numberOfAuthorisationReceived", "lastUpdatedDateTime", "expirationDateTime"]

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
        """Create an instance of MultiAuthorisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MultiAuthorisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "numberOfAuthorisationRequired": obj.get("numberOfAuthorisationRequired"),
            "numberOfAuthorisationReceived": obj.get("numberOfAuthorisationReceived"),
            "lastUpdatedDateTime": obj.get("lastUpdatedDateTime"),
            "expirationDateTime": obj.get("expirationDateTime")
        })
        return _obj


