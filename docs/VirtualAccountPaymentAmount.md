# VirtualAccountPaymentAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | __Mandatory__. The monetary value | 
**currency** | **str** | __Mandatory__. The [ISO 4217](https://www.xe.com/iso4217.php) currency code | 

## Example

```python
from yapily.models.virtual_account_payment_amount import VirtualAccountPaymentAmount

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPaymentAmount from a JSON string
virtual_account_payment_amount_instance = VirtualAccountPaymentAmount.from_json(json)
# print the JSON string representation of the object
print VirtualAccountPaymentAmount.to_json()

# convert the object into a dict
virtual_account_payment_amount_dict = virtual_account_payment_amount_instance.to_dict()
# create an instance of VirtualAccountPaymentAmount from a dict
virtual_account_payment_amount_form_dict = virtual_account_payment_amount.from_dict(virtual_account_payment_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


