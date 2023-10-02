# VirtualAccountBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter ISO 4217 currency code | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_address** | **str** |  | [optional] 
**bank_country** | **str** | Two-letter ISO 3166 country code | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | The account identifications that identify the Beneficiary bank account. | [optional] 
**pay_in_reference** | **str** | Reference required for paying into the account. When no reference is provided, then one is not required to pay into the acount. | [optional] 

## Example

```python
from yapily.models.virtual_account_bank_account import VirtualAccountBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBankAccount from a JSON string
virtual_account_bank_account_instance = VirtualAccountBankAccount.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBankAccount.to_json()

# convert the object into a dict
virtual_account_bank_account_dict = virtual_account_bank_account_instance.to_dict()
# create an instance of VirtualAccountBankAccount from a dict
virtual_account_bank_account_form_dict = virtual_account_bank_account.from_dict(virtual_account_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


