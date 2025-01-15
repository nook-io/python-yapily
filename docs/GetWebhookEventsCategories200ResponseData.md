# GetWebhookEventsCategories200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryStructure]**](CategoryStructure.md) |  | [optional] 

## Example

```python
from yapily.models.get_webhook_events_categories200_response_data import GetWebhookEventsCategories200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookEventsCategories200ResponseData from a JSON string
get_webhook_events_categories200_response_data_instance = GetWebhookEventsCategories200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetWebhookEventsCategories200ResponseData.to_json()

# convert the object into a dict
get_webhook_events_categories200_response_data_dict = get_webhook_events_categories200_response_data_instance.to_dict()
# create an instance of GetWebhookEventsCategories200ResponseData from a dict
get_webhook_events_categories200_response_data_from_dict = GetWebhookEventsCategories200ResponseData.from_dict(get_webhook_events_categories200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


