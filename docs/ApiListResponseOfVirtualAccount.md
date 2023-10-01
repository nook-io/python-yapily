# ApiListResponseOfVirtualAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**data** | [**List[VirtualAccount]**](VirtualAccount.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_virtual_account import ApiListResponseOfVirtualAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfVirtualAccount from a JSON string
api_list_response_of_virtual_account_instance = ApiListResponseOfVirtualAccount.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfVirtualAccount.to_json()

# convert the object into a dict
api_list_response_of_virtual_account_dict = api_list_response_of_virtual_account_instance.to_dict()
# create an instance of ApiListResponseOfVirtualAccount from a dict
api_list_response_of_virtual_account_form_dict = api_list_response_of_virtual_account.from_dict(api_list_response_of_virtual_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


