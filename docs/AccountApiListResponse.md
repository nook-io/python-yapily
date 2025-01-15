# AccountApiListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Account]**](Account.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListAccount**](FilteredClientPayloadListAccount.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.account_api_list_response import AccountApiListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountApiListResponse from a JSON string
account_api_list_response_instance = AccountApiListResponse.from_json(json)
# print the JSON string representation of the object
print AccountApiListResponse.to_json()

# convert the object into a dict
account_api_list_response_dict = account_api_list_response_instance.to_dict()
# create an instance of AccountApiListResponse from a dict
account_api_list_response_from_dict = AccountApiListResponse.from_dict(account_api_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


