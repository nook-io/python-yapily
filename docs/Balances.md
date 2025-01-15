# Balances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_balance_amount** | [**Amount**](Amount.md) |  | [optional] 
**balances** | [**List[AccountBalance]**](AccountBalance.md) |  | [optional] 

## Example

```python
from yapily.models.balances import Balances

# TODO update the JSON string below
json = "{}"
# create an instance of Balances from a JSON string
balances_instance = Balances.from_json(json)
# print the JSON string representation of the object
print(Balances.to_json())

# convert the object into a dict
balances_dict = balances_instance.to_dict()
# create an instance of Balances from a dict
balances_from_dict = Balances.from_dict(balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


