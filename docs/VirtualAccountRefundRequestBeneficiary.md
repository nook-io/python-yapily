# VirtualAccountRefundRequestBeneficiary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** | Reference that can be provided in order to help with identification of the Beneficiary | 
**type** | **str** | Indicates the type of Beneficiary as either an INDIVIDUAL or BUSINESS | 
**name** | **str** |  | 
**birth_date** | **date** |  | [optional] 
**payment_schemes** | **List[str]** | Beneficiary payment schemes | 
**address** | [**VirtualAccountBeneficiaryAddress**](VirtualAccountBeneficiaryAddress.md) |  | 
**account** | [**VirtualAccountBeneficiaryAccount**](VirtualAccountBeneficiaryAccount.md) |  | 

## Example

```python
from yapily.models.virtual_account_refund_request_beneficiary import VirtualAccountRefundRequestBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountRefundRequestBeneficiary from a JSON string
virtual_account_refund_request_beneficiary_instance = VirtualAccountRefundRequestBeneficiary.from_json(json)
# print the JSON string representation of the object
print VirtualAccountRefundRequestBeneficiary.to_json()

# convert the object into a dict
virtual_account_refund_request_beneficiary_dict = virtual_account_refund_request_beneficiary_instance.to_dict()
# create an instance of VirtualAccountRefundRequestBeneficiary from a dict
virtual_account_refund_request_beneficiary_form_dict = virtual_account_refund_request_beneficiary.from_dict(virtual_account_refund_request_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


