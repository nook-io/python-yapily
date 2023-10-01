# VirtualAccountBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**VirtualAccountBalanceType**](VirtualAccountBalanceType.md) |  | [optional] 
**balance_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from yapily.models.virtual_account_balance import VirtualAccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBalance from a JSON string
virtual_account_balance_instance = VirtualAccountBalance.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBalance.to_json()

# convert the object into a dict
virtual_account_balance_dict = virtual_account_balance_instance.to_dict()
# create an instance of VirtualAccountBalance from a dict
virtual_account_balance_form_dict = virtual_account_balance.from_dict(virtual_account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


