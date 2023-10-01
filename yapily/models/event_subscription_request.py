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



from pydantic import BaseModel, Field, StrictStr
from yapily.models.notification import Notification

class EventSubscriptionRequest(BaseModel):
    """
    EventSubscriptionRequest
    """
    event_type_id: StrictStr = Field(..., alias="eventTypeId", description="Unique identifier of the event type (for which notifications will be sent).<br><br>Allowed values: payment.status, payment.status.completed, payment.isoStatus, virtualAccount.payIn.status, virtualAccount.payOut.status, virtualAccount.createBeneficiary.status, virtualAccount.account.status, virtualAccount.client.status, virtualAccount.refund.status, virtualAccount.payOut.return  ")
    notification: Notification = Field(...)
    __properties = ["eventTypeId", "notification"]

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
    def from_json(cls, json_str: str) -> EventSubscriptionRequest:
        """Create an instance of EventSubscriptionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of notification
        if self.notification:
            _dict['notification'] = self.notification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventSubscriptionRequest:
        """Create an instance of EventSubscriptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventSubscriptionRequest.parse_obj(obj)

        _obj = EventSubscriptionRequest.parse_obj({
            "event_type_id": obj.get("eventTypeId"),
            "notification": Notification.from_dict(obj.get("notification")) if obj.get("notification") is not None else None
        })
        return _obj


