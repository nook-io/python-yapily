# TransactionBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountBalanceType**](AccountBalanceType.md) |  | [optional] 
**balance_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from yapily.models.transaction_balance import TransactionBalance

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBalance from a JSON string
transaction_balance_instance = TransactionBalance.from_json(json)
# print the JSON string representation of the object
print(TransactionBalance.to_json())

# convert the object into a dict
transaction_balance_dict = transaction_balance_instance.to_dict()
# create an instance of TransactionBalance from a dict
transaction_balance_from_dict = TransactionBalance.from_dict(transaction_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


