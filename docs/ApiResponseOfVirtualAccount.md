# ApiResponseOfVirtualAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**VirtualAccount**](VirtualAccount.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_virtual_account import ApiResponseOfVirtualAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfVirtualAccount from a JSON string
api_response_of_virtual_account_instance = ApiResponseOfVirtualAccount.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfVirtualAccount.to_json()

# convert the object into a dict
api_response_of_virtual_account_dict = api_response_of_virtual_account_instance.to_dict()
# create an instance of ApiResponseOfVirtualAccount from a dict
api_response_of_virtual_account_form_dict = api_response_of_virtual_account.from_dict(api_response_of_virtual_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


