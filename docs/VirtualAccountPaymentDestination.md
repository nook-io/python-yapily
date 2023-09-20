# VirtualAccountPaymentDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of destination for a payment. One of ACCOUNT, EXTERNAL or BENEFICIARY | 
**account_id** | **str** | Only present if type is ACCOUNT. Identifies the Virtual Account to which the payment was made | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | Only present if type is EXTERNAL. The account identifications that identify an external destination | [optional] 
**beneficiary_id** | **str** | Only present if type is BENEFICIARY. Unique id of the beneficiary | [optional] 

## Example

```python
from yapily.models.virtual_account_payment_destination import VirtualAccountPaymentDestination

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPaymentDestination from a JSON string
virtual_account_payment_destination_instance = VirtualAccountPaymentDestination.from_json(json)
# print the JSON string representation of the object
print VirtualAccountPaymentDestination.to_json()

# convert the object into a dict
virtual_account_payment_destination_dict = virtual_account_payment_destination_instance.to_dict()
# create an instance of VirtualAccountPaymentDestination from a dict
virtual_account_payment_destination_form_dict = virtual_account_payment_destination.from_dict(virtual_account_payment_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


