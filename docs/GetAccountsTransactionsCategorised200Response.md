# GetAccountsTransactionsCategorised200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetAccountsTransactionsCategorised200ResponseMeta**](GetAccountsTransactionsCategorised200ResponseMeta.md) |  | [optional] 
**data** | [**GetAccountsTransactionsCategorised200ResponseData**](GetAccountsTransactionsCategorised200ResponseData.md) |  | [optional] 
**links** | [**GetAccountsTransactionsCategorised200ResponseLinks**](GetAccountsTransactionsCategorised200ResponseLinks.md) |  | [optional] 

## Example

```python
from yapily.models.get_accounts_transactions_categorised200_response import GetAccountsTransactionsCategorised200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTransactionsCategorised200Response from a JSON string
get_accounts_transactions_categorised200_response_instance = GetAccountsTransactionsCategorised200Response.from_json(json)
# print the JSON string representation of the object
print GetAccountsTransactionsCategorised200Response.to_json()

# convert the object into a dict
get_accounts_transactions_categorised200_response_dict = get_accounts_transactions_categorised200_response_instance.to_dict()
# create an instance of GetAccountsTransactionsCategorised200Response from a dict
get_accounts_transactions_categorised200_response_from_dict = GetAccountsTransactionsCategorised200Response.from_dict(get_accounts_transactions_categorised200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


