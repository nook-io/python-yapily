# VirtualAccountBeneficiary



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the Beneficiary | [optional] 
**payment_schemes** | **List[str]** | Beneficiary payment schemes | [optional] 
**nickname** | **str** | Reference that can be provided in order to help with identification of the Beneficiary | [optional] 
**type** | **str** | Indicates the type of Beneficiary as either a INDIVIDUAL or BUSINESS | [optional] 
**name** | **str** |  | [optional] 
**birth_date** | **date** |  | [optional] 
**address** | [**VirtualAccountBeneficiaryAddress**](VirtualAccountBeneficiaryAddress.md) |  | [optional] 
**account** | [**VirtualAccountBeneficiaryAccount**](VirtualAccountBeneficiaryAccount.md) |  | [optional] 
**status** | **str** | The current status of the Beneficiary &lt;br&gt; PENDING - Beneficiary is awaiting verification &lt;br&gt; ACTIVE - Beneficiary can be used in a Pay Out &lt;br&gt; BLOCKED - Beneficiary cannot be used in a Pay Out | [optional] 

## Example

```python
from yapily.models.virtual_account_beneficiary import VirtualAccountBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBeneficiary from a JSON string
virtual_account_beneficiary_instance = VirtualAccountBeneficiary.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBeneficiary.to_json()

# convert the object into a dict
virtual_account_beneficiary_dict = virtual_account_beneficiary_instance.to_dict()
# create an instance of VirtualAccountBeneficiary from a dict
virtual_account_beneficiary_form_dict = virtual_account_beneficiary.from_dict(virtual_account_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


