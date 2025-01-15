# RegisterWebhook201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**data** | [**RegisterWebhook201ResponseData**](RegisterWebhook201ResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.register_webhook201_response import RegisterWebhook201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterWebhook201Response from a JSON string
register_webhook201_response_instance = RegisterWebhook201Response.from_json(json)
# print the JSON string representation of the object
print(RegisterWebhook201Response.to_json())

# convert the object into a dict
register_webhook201_response_dict = register_webhook201_response_instance.to_dict()
# create an instance of RegisterWebhook201Response from a dict
register_webhook201_response_from_dict = RegisterWebhook201Response.from_dict(register_webhook201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


