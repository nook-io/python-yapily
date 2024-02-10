# ApiResponseOfVirtualAccountClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**VirtualAccountClient**](VirtualAccountClient.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_virtual_account_client import ApiResponseOfVirtualAccountClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfVirtualAccountClient from a JSON string
api_response_of_virtual_account_client_instance = ApiResponseOfVirtualAccountClient.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfVirtualAccountClient.to_json()

# convert the object into a dict
api_response_of_virtual_account_client_dict = api_response_of_virtual_account_client_instance.to_dict()
# create an instance of ApiResponseOfVirtualAccountClient from a dict
api_response_of_virtual_account_client_form_dict = api_response_of_virtual_account_client.from_dict(api_response_of_virtual_account_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


