# ApiListResponseOfAccountStatement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[AccountStatement]**](AccountStatement.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListAccountStatement**](FilteredClientPayloadListAccountStatement.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_account_statement import ApiListResponseOfAccountStatement

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfAccountStatement from a JSON string
api_list_response_of_account_statement_instance = ApiListResponseOfAccountStatement.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfAccountStatement.to_json()

# convert the object into a dict
api_list_response_of_account_statement_dict = api_list_response_of_account_statement_instance.to_dict()
# create an instance of ApiListResponseOfAccountStatement from a dict
api_list_response_of_account_statement_form_dict = api_list_response_of_account_statement.from_dict(api_list_response_of_account_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


