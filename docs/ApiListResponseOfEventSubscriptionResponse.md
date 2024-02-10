# ApiListResponseOfEventSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[EventSubscriptionResponse]**](EventSubscriptionResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListTransaction**](FilteredClientPayloadListTransaction.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_event_subscription_response import ApiListResponseOfEventSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfEventSubscriptionResponse from a JSON string
api_list_response_of_event_subscription_response_instance = ApiListResponseOfEventSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfEventSubscriptionResponse.to_json()

# convert the object into a dict
api_list_response_of_event_subscription_response_dict = api_list_response_of_event_subscription_response_instance.to_dict()
# create an instance of ApiListResponseOfEventSubscriptionResponse from a dict
api_list_response_of_event_subscription_response_form_dict = api_list_response_of_event_subscription_response.from_dict(api_list_response_of_event_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


