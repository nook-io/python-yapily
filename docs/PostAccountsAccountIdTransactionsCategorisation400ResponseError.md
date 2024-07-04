# PostAccountsAccountIdTransactionsCategorisation400ResponseError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | [optional] 
**code** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**support_url** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**issues** | [**List[PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner]**](PostAccountsAccountIdTransactionsCategorisation400ResponseErrorIssuesInner.md) |  | [optional] 

## Example

```python
from yapily.models.post_accounts_account_id_transactions_categorisation400_response_error import PostAccountsAccountIdTransactionsCategorisation400ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseError from a JSON string
post_accounts_account_id_transactions_categorisation400_response_error_instance = PostAccountsAccountIdTransactionsCategorisation400ResponseError.from_json(json)
# print the JSON string representation of the object
print PostAccountsAccountIdTransactionsCategorisation400ResponseError.to_json()

# convert the object into a dict
post_accounts_account_id_transactions_categorisation400_response_error_dict = post_accounts_account_id_transactions_categorisation400_response_error_instance.to_dict()
# create an instance of PostAccountsAccountIdTransactionsCategorisation400ResponseError from a dict
post_accounts_account_id_transactions_categorisation400_response_error_form_dict = post_accounts_account_id_transactions_categorisation400_response_error.from_dict(post_accounts_account_id_transactions_categorisation400_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


