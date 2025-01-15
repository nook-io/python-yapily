# GetAccountsTransactionsCategorised200ResponseDataTransactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**booking_date_time** | **datetime** |  | [optional] 
**value_date_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**transaction_amount** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerTransactionAmount.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**transaction_information** | **List[str]** |  | [optional] 
**proprietary_bank_transaction_code** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerProprietaryBankTransactionCode.md) |  | [optional] 
**iso_bank_transaction_code** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerIsoBankTransactionCode.md) |  | [optional] 
**balance** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerBalance.md) |  | [optional] 
**enrichment** | [**GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment**](GetAccountsTransactionsCategorised200ResponseDataTransactionsInnerEnrichment.md) |  | [optional] 
**hash** | **str** |  | [optional] 

## Example

```python
from yapily.models.get_accounts_transactions_categorised200_response_data_transactions_inner import GetAccountsTransactionsCategorised200ResponseDataTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInner from a JSON string
get_accounts_transactions_categorised200_response_data_transactions_inner_instance = GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.to_json())

# convert the object into a dict
get_accounts_transactions_categorised200_response_data_transactions_inner_dict = get_accounts_transactions_categorised200_response_data_transactions_inner_instance.to_dict()
# create an instance of GetAccountsTransactionsCategorised200ResponseDataTransactionsInner from a dict
get_accounts_transactions_categorised200_response_data_transactions_inner_from_dict = GetAccountsTransactionsCategorised200ResponseDataTransactionsInner.from_dict(get_accounts_transactions_categorised200_response_data_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


