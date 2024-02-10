# VirtualAccountBeneficiaryAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line** | **str** |  | [optional] 
**town_name** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**country** | **str** | Two-letter ISO 3166 country code | 

## Example

```python
from yapily.models.virtual_account_beneficiary_address import VirtualAccountBeneficiaryAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBeneficiaryAddress from a JSON string
virtual_account_beneficiary_address_instance = VirtualAccountBeneficiaryAddress.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBeneficiaryAddress.to_json()

# convert the object into a dict
virtual_account_beneficiary_address_dict = virtual_account_beneficiary_address_instance.to_dict()
# create an instance of VirtualAccountBeneficiaryAddress from a dict
virtual_account_beneficiary_address_form_dict = virtual_account_beneficiary_address.from_dict(virtual_account_beneficiary_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


