# PaymentIsoStatus

The payment status code, as denoted by a 3-letter ISO 20022 code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**PaymentIsoStatusCodeEnum**](PaymentIsoStatusCodeEnum.md) |  | [optional] 
**name** | **str** | The full name of the ISO 20022 &#x60;PaymentStatusCode&#x60;. | [optional] 

## Example

```python
from yapily.models.payment_iso_status import PaymentIsoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIsoStatus from a JSON string
payment_iso_status_instance = PaymentIsoStatus.from_json(json)
# print the JSON string representation of the object
print PaymentIsoStatus.to_json()

# convert the object into a dict
payment_iso_status_dict = payment_iso_status_instance.to_dict()
# create an instance of PaymentIsoStatus from a dict
payment_iso_status_form_dict = payment_iso_status.from_dict(payment_iso_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


