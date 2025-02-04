# ApiResponseOfAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**Account**](Account.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_account import ApiResponseOfAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfAccount from a JSON string
api_response_of_account_instance = ApiResponseOfAccount.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfAccount.to_json()

# convert the object into a dict
api_response_of_account_dict = api_response_of_account_instance.to_dict()
# create an instance of ApiResponseOfAccount from a dict
api_response_of_account_from_dict = ApiResponseOfAccount.from_dict(api_response_of_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


