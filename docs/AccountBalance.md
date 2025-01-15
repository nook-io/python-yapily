# AccountBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountBalanceType**](AccountBalanceType.md) |  | [optional] 
**date_time** | **datetime** | Date and time of the reported balance. | [optional] 
**balance_amount** | [**Amount**](Amount.md) |  | [optional] 
**credit_line_included** | **bool** | _Optional_. Indicates whether any credit lines are included in the balance. | [optional] 
**credit_lines** | [**List[CreditLine]**](CreditLine.md) | _Optional_. Specifies the type of balance. | [optional] 

## Example

```python
from yapily.models.account_balance import AccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBalance from a JSON string
account_balance_instance = AccountBalance.from_json(json)
# print the JSON string representation of the object
print AccountBalance.to_json()

# convert the object into a dict
account_balance_dict = account_balance_instance.to_dict()
# create an instance of AccountBalance from a dict
account_balance_from_dict = AccountBalance.from_dict(account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


