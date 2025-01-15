# ApiListResponseOfDirectDebitResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[DirectDebitResponse]**](DirectDebitResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListDirectDebitResponse**](FilteredClientPayloadListDirectDebitResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_direct_debit_response import ApiListResponseOfDirectDebitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfDirectDebitResponse from a JSON string
api_list_response_of_direct_debit_response_instance = ApiListResponseOfDirectDebitResponse.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfDirectDebitResponse.to_json()

# convert the object into a dict
api_list_response_of_direct_debit_response_dict = api_list_response_of_direct_debit_response_instance.to_dict()
# create an instance of ApiListResponseOfDirectDebitResponse from a dict
api_list_response_of_direct_debit_response_from_dict = ApiListResponseOfDirectDebitResponse.from_dict(api_list_response_of_direct_debit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


