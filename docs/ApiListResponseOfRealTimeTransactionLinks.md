# ApiListResponseOfRealTimeTransactionLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | A cursor or link to the first page in the data set. | [optional] 
**prev** | **str** | A cursor or link to the previous page in the data set. | [optional] 
**var_self** | **str** | A cursor or link to the current page in the data set. | [optional] 
**next** | **str** | A cursor or link to the next page in the data set. | [optional] 
**last** | **str** | A cursor or link to the last page in the data set. | [optional] 

## Example

```python
from yapily.models.api_list_response_of_real_time_transaction_links import ApiListResponseOfRealTimeTransactionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfRealTimeTransactionLinks from a JSON string
api_list_response_of_real_time_transaction_links_instance = ApiListResponseOfRealTimeTransactionLinks.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfRealTimeTransactionLinks.to_json()

# convert the object into a dict
api_list_response_of_real_time_transaction_links_dict = api_list_response_of_real_time_transaction_links_instance.to_dict()
# create an instance of ApiListResponseOfRealTimeTransactionLinks from a dict
api_list_response_of_real_time_transaction_links_from_dict = ApiListResponseOfRealTimeTransactionLinks.from_dict(api_list_response_of_real_time_transaction_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


