# HostedPaymentStatusDetails

The status of the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_update_date** | **datetime** | Date and time the status was updated. | [optional] 
**iso_status** | [**HostedPaymentIsoStatus**](HostedPaymentIsoStatus.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentStatusDetails from a JSON string
hosted_payment_status_details_instance = HostedPaymentStatusDetails.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentStatusDetails.to_json())

# convert the object into a dict
hosted_payment_status_details_dict = hosted_payment_status_details_instance.to_dict()
# create an instance of HostedPaymentStatusDetails from a dict
hosted_payment_status_details_from_dict = HostedPaymentStatusDetails.from_dict(hosted_payment_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


