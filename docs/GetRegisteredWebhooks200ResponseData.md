# GetRegisteredWebhooks200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[RegisteredWebhookWithStatus]**](RegisteredWebhookWithStatus.md) |  | [optional] 

## Example

```python
from yapily.models.get_registered_webhooks200_response_data import GetRegisteredWebhooks200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegisteredWebhooks200ResponseData from a JSON string
get_registered_webhooks200_response_data_instance = GetRegisteredWebhooks200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRegisteredWebhooks200ResponseData.to_json())

# convert the object into a dict
get_registered_webhooks200_response_data_dict = get_registered_webhooks200_response_data_instance.to_dict()
# create an instance of GetRegisteredWebhooks200ResponseData from a dict
get_registered_webhooks200_response_data_from_dict = GetRegisteredWebhooks200ResponseData.from_dict(get_registered_webhooks200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


