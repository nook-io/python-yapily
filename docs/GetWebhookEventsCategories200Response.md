# GetWebhookEventsCategories200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**data** | [**GetWebhookEventsCategories200ResponseData**](GetWebhookEventsCategories200ResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.get_webhook_events_categories200_response import GetWebhookEventsCategories200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookEventsCategories200Response from a JSON string
get_webhook_events_categories200_response_instance = GetWebhookEventsCategories200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebhookEventsCategories200Response.to_json())

# convert the object into a dict
get_webhook_events_categories200_response_dict = get_webhook_events_categories200_response_instance.to_dict()
# create an instance of GetWebhookEventsCategories200Response from a dict
get_webhook_events_categories200_response_from_dict = GetWebhookEventsCategories200Response.from_dict(get_webhook_events_categories200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


