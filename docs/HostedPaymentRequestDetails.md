# HostedPaymentRequestDetails

Details of the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | 
**reference** | **str** | The payment reference or description. Limited to a maximum of 18 characters for UK institutions. | [optional] 
**context_type** | [**PaymentContextType**](PaymentContextType.md) |  | [optional] [default to PaymentContextType.OTHER]
**type** | [**PaymentType**](PaymentType.md) |  | 
**payee** | [**Payee**](Payee.md) |  | 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**amount_details** | [**HostedAmountDetails**](HostedAmountDetails.md) |  | 
**payment_due_date** | **date** | The date that the payment is due. Displayed to the end user in the payment summary screen. | [optional] 

## Example

```python
from yapily.models.hosted_payment_request_details import HostedPaymentRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentRequestDetails from a JSON string
hosted_payment_request_details_instance = HostedPaymentRequestDetails.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentRequestDetails.to_json())

# convert the object into a dict
hosted_payment_request_details_dict = hosted_payment_request_details_instance.to_dict()
# create an instance of HostedPaymentRequestDetails from a dict
hosted_payment_request_details_from_dict = HostedPaymentRequestDetails.from_dict(hosted_payment_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


