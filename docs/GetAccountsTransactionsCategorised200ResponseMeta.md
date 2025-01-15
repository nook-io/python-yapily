# GetAccountsTransactionsCategorised200ResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | [optional] 
**count** | **int** | total number of transactions available | [optional] 
**page_count** | **int** | total number of pages available calculated based on the limit per page sent in the request | [optional] 

## Example

```python
from yapily.models.get_accounts_transactions_categorised200_response_meta import GetAccountsTransactionsCategorised200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTransactionsCategorised200ResponseMeta from a JSON string
get_accounts_transactions_categorised200_response_meta_instance = GetAccountsTransactionsCategorised200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetAccountsTransactionsCategorised200ResponseMeta.to_json()

# convert the object into a dict
get_accounts_transactions_categorised200_response_meta_dict = get_accounts_transactions_categorised200_response_meta_instance.to_dict()
# create an instance of GetAccountsTransactionsCategorised200ResponseMeta from a dict
get_accounts_transactions_categorised200_response_meta_from_dict = GetAccountsTransactionsCategorised200ResponseMeta.from_dict(get_accounts_transactions_categorised200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


