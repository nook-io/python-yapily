# EventSubscriptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** | Unique identifier of the event type (for which notifications will be sent) | 
**application_id** | **str** | Application related to event subscription. | 
**created** | **str** | Creation date of event subscription. | 
**notification** | [**Notification**](Notification.md) |  | 

## Example

```python
from yapily.models.event_subscription_response import EventSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscriptionResponse from a JSON string
event_subscription_response_instance = EventSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print EventSubscriptionResponse.to_json()

# convert the object into a dict
event_subscription_response_dict = event_subscription_response_instance.to_dict()
# create an instance of EventSubscriptionResponse from a dict
event_subscription_response_from_dict = EventSubscriptionResponse.from_dict(event_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


