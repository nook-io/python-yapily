# ApiListResponseOfTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListTransaction**](FilteredClientPayloadListTransaction.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfTransaction from a JSON string
api_list_response_of_transaction_instance = ApiListResponseOfTransaction.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfTransaction.to_json())

# convert the object into a dict
api_list_response_of_transaction_dict = api_list_response_of_transaction_instance.to_dict()
# create an instance of ApiListResponseOfTransaction from a dict
api_list_response_of_transaction_from_dict = ApiListResponseOfTransaction.from_dict(api_list_response_of_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


