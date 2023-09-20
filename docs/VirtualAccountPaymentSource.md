# VirtualAccountPaymentSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of source for a payment. One of ACCOUNT or EXTERNAL | 
**account_id** | **str** | Only present if type is ACCOUNT. Identifies the Virtual Account from which the payment was made | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | Only present if type is EXTERNAL. The account identifications that identify an external source | [optional] 

## Example

```python
from yapily.models.virtual_account_payment_source import VirtualAccountPaymentSource

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPaymentSource from a JSON string
virtual_account_payment_source_instance = VirtualAccountPaymentSource.from_json(json)
# print the JSON string representation of the object
print VirtualAccountPaymentSource.to_json()

# convert the object into a dict
virtual_account_payment_source_dict = virtual_account_payment_source_instance.to_dict()
# create an instance of VirtualAccountPaymentSource from a dict
virtual_account_payment_source_form_dict = virtual_account_payment_source.from_dict(virtual_account_payment_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


