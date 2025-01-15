# GetRegisteredWebhooks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**data** | [**GetRegisteredWebhooks200ResponseData**](GetRegisteredWebhooks200ResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.get_registered_webhooks200_response import GetRegisteredWebhooks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegisteredWebhooks200Response from a JSON string
get_registered_webhooks200_response_instance = GetRegisteredWebhooks200Response.from_json(json)
# print the JSON string representation of the object
print(GetRegisteredWebhooks200Response.to_json())

# convert the object into a dict
get_registered_webhooks200_response_dict = get_registered_webhooks200_response_instance.to_dict()
# create an instance of GetRegisteredWebhooks200Response from a dict
get_registered_webhooks200_response_from_dict = GetRegisteredWebhooks200Response.from_dict(get_registered_webhooks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


