# ApiListResponseOfRealTimeTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMetaWithCount**](ResponseMetaWithCount.md) |  | [optional] 
**data** | [**List[RealTimeTransaction]**](RealTimeTransaction.md) |  | [optional] 
**links** | [**ApiListResponseOfRealTimeTransactionLinks**](ApiListResponseOfRealTimeTransactionLinks.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_real_time_transaction import ApiListResponseOfRealTimeTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfRealTimeTransaction from a JSON string
api_list_response_of_real_time_transaction_instance = ApiListResponseOfRealTimeTransaction.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfRealTimeTransaction.to_json()

# convert the object into a dict
api_list_response_of_real_time_transaction_dict = api_list_response_of_real_time_transaction_instance.to_dict()
# create an instance of ApiListResponseOfRealTimeTransaction from a dict
api_list_response_of_real_time_transaction_from_dict = ApiListResponseOfRealTimeTransaction.from_dict(api_list_response_of_real_time_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


