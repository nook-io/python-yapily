# ConsolidatedAccountInformation

Summary information regarding account balances of the overall account provided by the bank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the consolidated account. When used in Get Account Transactions calls, the transactions between the sub-accounts will not be reported | [optional] 
**account_balances** | [**List[AccountBalance]**](AccountBalance.md) |  | [optional] 

## Example

```python
from yapily.models.consolidated_account_information import ConsolidatedAccountInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAccountInformation from a JSON string
consolidated_account_information_instance = ConsolidatedAccountInformation.from_json(json)
# print the JSON string representation of the object
print ConsolidatedAccountInformation.to_json()

# convert the object into a dict
consolidated_account_information_dict = consolidated_account_information_instance.to_dict()
# create an instance of ConsolidatedAccountInformation from a dict
consolidated_account_information_form_dict = consolidated_account_information.from_dict(consolidated_account_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


