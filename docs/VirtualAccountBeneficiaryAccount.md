# VirtualAccountBeneficiaryAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter ISO 4217 currency code | 
**bank_name** | **str** |  | [optional] 
**bank_address** | **str** |  | [optional] 
**bank_country** | **str** | Two-letter ISO 3166 country code | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | The account identifications that identify the Beneficiary bank account. | 

## Example

```python
from yapily.models.virtual_account_beneficiary_account import VirtualAccountBeneficiaryAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBeneficiaryAccount from a JSON string
virtual_account_beneficiary_account_instance = VirtualAccountBeneficiaryAccount.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBeneficiaryAccount.to_json()

# convert the object into a dict
virtual_account_beneficiary_account_dict = virtual_account_beneficiary_account_instance.to_dict()
# create an instance of VirtualAccountBeneficiaryAccount from a dict
virtual_account_beneficiary_account_form_dict = virtual_account_beneficiary_account.from_dict(virtual_account_beneficiary_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


