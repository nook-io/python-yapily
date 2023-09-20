# ApiListResponseOfVirtualAccountClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[VirtualAccountClient]**](VirtualAccountClient.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_virtual_account_client import ApiListResponseOfVirtualAccountClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfVirtualAccountClient from a JSON string
api_list_response_of_virtual_account_client_instance = ApiListResponseOfVirtualAccountClient.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfVirtualAccountClient.to_json()

# convert the object into a dict
api_list_response_of_virtual_account_client_dict = api_list_response_of_virtual_account_client_instance.to_dict()
# create an instance of ApiListResponseOfVirtualAccountClient from a dict
api_list_response_of_virtual_account_client_form_dict = api_list_response_of_virtual_account_client.from_dict(api_list_response_of_virtual_account_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


