# ApiResponseOfAccountStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**AccountStatement**](AccountStatement.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_account_statement import ApiResponseOfAccountStatement

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfAccountStatement from a JSON string
api_response_of_account_statement_instance = ApiResponseOfAccountStatement.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfAccountStatement.to_json())

# convert the object into a dict
api_response_of_account_statement_dict = api_response_of_account_statement_instance.to_dict()
# create an instance of ApiResponseOfAccountStatement from a dict
api_response_of_account_statement_from_dict = ApiResponseOfAccountStatement.from_dict(api_response_of_account_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


