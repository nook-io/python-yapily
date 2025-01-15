# EventSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** | Unique identifier of the event type (for which notifications will be sent).&lt;br&gt;&lt;br&gt;Allowed values: payment.status, payment.status.completed, payment.isoStatus  | 
**notification** | [**Notification**](Notification.md) |  | 

## Example

```python
from yapily.models.event_subscription_request import EventSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscriptionRequest from a JSON string
event_subscription_request_instance = EventSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(EventSubscriptionRequest.to_json())

# convert the object into a dict
event_subscription_request_dict = event_subscription_request_instance.to_dict()
# create an instance of EventSubscriptionRequest from a dict
event_subscription_request_from_dict = EventSubscriptionRequest.from_dict(event_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


