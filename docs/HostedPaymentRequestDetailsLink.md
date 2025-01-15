# HostedPaymentRequestDetailsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The payment reference or description. Limited to a maximum of 18 characters for UK institutions. | [optional] 
**context_type** | [**PaymentContextTypeResponse**](PaymentContextTypeResponse.md) |  | [optional] 
**type** | [**PaymentTypeResponse**](PaymentTypeResponse.md) |  | [optional] 
**payee** | [**PayeeDetailsResponse**](PayeeDetailsResponse.md) |  | [optional] 
**payer** | [**PayerDetailsResponse**](PayerDetailsResponse.md) |  | [optional] 
**amount_details** | [**AmountDetailsResponse**](AmountDetailsResponse.md) |  | [optional] 
**payment_due_date** | **date** | The date that the payment is due. Displayed to the end user in the payment summary screen. | [optional] 

## Example

```python
from yapily.models.hosted_payment_request_details_link import HostedPaymentRequestDetailsLink

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentRequestDetailsLink from a JSON string
hosted_payment_request_details_link_instance = HostedPaymentRequestDetailsLink.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentRequestDetailsLink.to_json())

# convert the object into a dict
hosted_payment_request_details_link_dict = hosted_payment_request_details_link_instance.to_dict()
# create an instance of HostedPaymentRequestDetailsLink from a dict
hosted_payment_request_details_link_from_dict = HostedPaymentRequestDetailsLink.from_dict(hosted_payment_request_details_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


