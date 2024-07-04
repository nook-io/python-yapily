# EventSubscriptionDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** | Unique identifier of the event type (for which notifications will be sent) | 
**application_id** | **str** | Application related to event subscription. | 
**created** | **datetime** | Creation datetime of event subscription. | 
**delete_status** | [**DeleteStatusEnum**](DeleteStatusEnum.md) |  | 

## Example

```python
from yapily.models.event_subscription_delete_response import EventSubscriptionDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscriptionDeleteResponse from a JSON string
event_subscription_delete_response_instance = EventSubscriptionDeleteResponse.from_json(json)
# print the JSON string representation of the object
print EventSubscriptionDeleteResponse.to_json()

# convert the object into a dict
event_subscription_delete_response_dict = event_subscription_delete_response_instance.to_dict()
# create an instance of EventSubscriptionDeleteResponse from a dict
event_subscription_delete_response_form_dict = event_subscription_delete_response.from_dict(event_subscription_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


