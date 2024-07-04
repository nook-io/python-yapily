# PostAccountsAccountIdTransactionsCategorisationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | _Mandatory_, ISO 3166-1 alpha-2 two-letter country codes e.g. GB | 
**var_from** | **datetime** | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
**before** | **datetime** | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
**sort** | **str** | __Optional__. Sort transaction records by date ascending with &#39;date&#39; or descending with &#39;-date&#39;. The default sort order is descending | [optional] 

## Example

```python
from yapily.models.post_accounts_account_id_transactions_categorisation_request import PostAccountsAccountIdTransactionsCategorisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsAccountIdTransactionsCategorisationRequest from a JSON string
post_accounts_account_id_transactions_categorisation_request_instance = PostAccountsAccountIdTransactionsCategorisationRequest.from_json(json)
# print the JSON string representation of the object
print PostAccountsAccountIdTransactionsCategorisationRequest.to_json()

# convert the object into a dict
post_accounts_account_id_transactions_categorisation_request_dict = post_accounts_account_id_transactions_categorisation_request_instance.to_dict()
# create an instance of PostAccountsAccountIdTransactionsCategorisationRequest from a dict
post_accounts_account_id_transactions_categorisation_request_form_dict = post_accounts_account_id_transactions_categorisation_request.from_dict(post_accounts_account_id_transactions_categorisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


