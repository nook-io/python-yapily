# PaymentChargeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_amount** | [**Amount**](Amount.md) |  | [optional] 
**charge_type** | **str** | Type of charge | [optional] 
**charge_to** | **str** | Charge bearer | [optional] 

## Example

```python
from yapily.models.payment_charge_details import PaymentChargeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentChargeDetails from a JSON string
payment_charge_details_instance = PaymentChargeDetails.from_json(json)
# print the JSON string representation of the object
print PaymentChargeDetails.to_json()

# convert the object into a dict
payment_charge_details_dict = payment_charge_details_instance.to_dict()
# create an instance of PaymentChargeDetails from a dict
payment_charge_details_form_dict = payment_charge_details.from_dict(payment_charge_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


