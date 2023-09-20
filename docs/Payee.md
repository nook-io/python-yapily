# Payee

__Mandatory__. The `Payee` object contains details of the beneficiary [person or business]. You must define this in your payment request alongwith all of the nested mandatory properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __Mandatory__. The account holder name of the beneficiary. | 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payee&#x60; bank account. | 
**address** | [**Address**](Address.md) |  | [optional] 
**merchant_id** | **str** | __Optional__. The merchant ID is a unique code provided by the payment processor to the merchant. | [optional] 
**merchant_category_code** | **str** | __Optional__. The category code of the merchant in case the &#x60;Payee&#x60; is a business. | [optional] 

## Example

```python
from yapily.models.payee import Payee

# TODO update the JSON string below
json = "{}"
# create an instance of Payee from a JSON string
payee_instance = Payee.from_json(json)
# print the JSON string representation of the object
print Payee.to_json()

# convert the object into a dict
payee_dict = payee_instance.to_dict()
# create an instance of Payee from a dict
payee_form_dict = payee.from_dict(payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


