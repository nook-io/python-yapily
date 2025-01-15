# HostedPaymentResponseDetails

Details of the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | A unique identifier provided to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | [optional] 
**reference** | **str** | The payment reference or description. Limited to a maximum of 18 characters for UK institutions. | [optional] 
**context_type** | [**PaymentContextTypeResponse**](PaymentContextTypeResponse.md) |  | [optional] 
**type** | [**PaymentTypeResponse**](PaymentTypeResponse.md) |  | [optional] 
**payee** | [**PayeeDetailsResponse**](PayeeDetailsResponse.md) |  | [optional] 
**payer** | [**PayerDetailsResponse**](PayerDetailsResponse.md) |  | [optional] 
**amount_details** | [**AmountDetailsResponse**](AmountDetailsResponse.md) |  | [optional] 
**payment_due_date** | **date** | The date that the payment is due. | [optional] 

## Example

```python
from yapily.models.hosted_payment_response_details import HostedPaymentResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentResponseDetails from a JSON string
hosted_payment_response_details_instance = HostedPaymentResponseDetails.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentResponseDetails.to_json())

# convert the object into a dict
hosted_payment_response_details_dict = hosted_payment_response_details_instance.to_dict()
# create an instance of HostedPaymentResponseDetails from a dict
hosted_payment_response_details_from_dict = HostedPaymentResponseDetails.from_dict(hosted_payment_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


