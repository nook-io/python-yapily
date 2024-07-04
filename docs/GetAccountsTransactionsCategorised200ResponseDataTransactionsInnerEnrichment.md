# GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorisation** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentCategorisation.md) |  | [optional] 
**recurrence** | **str** |  | [optional] 
**transaction_hash** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentTransactionHash.md) |  | [optional] 
**merchant** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichmentMerchant.md) |  | [optional] 
**payment_processor** | **str** |  | [optional] 

## Example

```python
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment import GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment from a JSON string
get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_instance = GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.from_json(json)
# print the JSON string representation of the object
print GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.to_json()

# convert the object into a dict
get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_dict = get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_instance.to_dict()
# create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment from a dict
get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_form_dict = get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment.from_dict(get_accounts_transactions_categorised200_response_data_transactions_inner_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


