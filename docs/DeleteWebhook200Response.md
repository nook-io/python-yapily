# DeleteWebhook200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**data** | [**RegisteredWebhook**](RegisteredWebhook.md) |  | [optional] 

## Example

```python
from yapily.models.delete_webhook200_response import DeleteWebhook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhook200Response from a JSON string
delete_webhook200_response_instance = DeleteWebhook200Response.from_json(json)
# print the JSON string representation of the object
print DeleteWebhook200Response.to_json()

# convert the object into a dict
delete_webhook200_response_dict = delete_webhook200_response_instance.to_dict()
# create an instance of DeleteWebhook200Response from a dict
delete_webhook200_response_from_dict = DeleteWebhook200Response.from_dict(delete_webhook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


